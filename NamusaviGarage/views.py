from django.shortcuts import render, redirect
from .models import NamusaviGarage

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        make = request.POST.get('make')
        model = request.POST.get('model')
        chasis = request.POST.get('chasis')
        damage = request.POST.get('damage')
        insuarance = request.POST.get('insuarance')

        query = NamusaviGarage.objects.create(name=name, email=email, phone=phone, make=make, model=model, chasis=chasis, damage=damage, insuarance=insuarance)

        query.save()
    return redirect("/")
    return render(request, "index.html")

def indexpage(request):
    dta = NamusaviGarage.objects.all()
    context = {"dta": dta}
    return render(request, "index.html", context)

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        make = request.POST.get('make')
        model = request.POST.get('model')
        chasis = request.POST.get('chasis')
        damage = request.POST.get('damage')
        insuarance = request.POST.get('insuarance')

        edit_data = NamusaviGarage.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.phone = phone
        edit_data.make = make
        edit_data.model = model
        edit_data.chasis = chasis
        edit_data.damage = damage
        edit_data.insuarance = insuarance
        edit_data.save()
    return redirect("/")

    dta = NamusaviGarage.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)

def deleteData(request, id):
    d = NamusaviGarage.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")