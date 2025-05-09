from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Module
from django.conf import settings
from django.core import management
from django.conf import settings

app2url = {
    "sample_module":"/product"
}

def module_list(request):
    modules = Module.objects.all()
    print("settings.INSTALLED_APPS")
    modules_list = list(modules.values())
    for module in modules_list:
        module_name = module['name']
        if module_name in app2url:
            module['url'] = app2url[module_name]
        else:
            module['url'] = "/module"
    
    print(modules_list)

    return render(request, 'modular_engine/module_list.html', {'modules': modules_list})

def install_module(request, mod_id):
    mod = Module.objects.get(id=mod_id)
    management.call_command('migrate', mod.name)
    if mod.name not in settings.INSTALLED_APPS: 
        settings.INSTALLED_APPS.append(mod.name)

    mod.installed = True
    mod.save()
    return redirect('module_list')

def uninstall_module(request, mod_id):
    mod = Module.objects.get(id=mod_id)
    management.call_command('migrate', mod.name, 'zero')
    settings.INSTALLED_APPS.remove(mod.name)
    mod.installed = False
    mod.save()
    return redirect('module_list')

def upgrade_module(request, mod_id):
    mod = Module.objects.get(id=mod_id)
    management.call_command('makemigrations', mod.name)
    management.call_command('migrate', mod.name)
    # Anda bisa menambah logika cek versi di sini
    return redirect('module_list')