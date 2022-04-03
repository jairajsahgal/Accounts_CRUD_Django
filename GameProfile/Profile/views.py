from django.shortcuts import render, redirect, HttpResponse
from .models import Account
from .forms import AccountForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AccountSerializer


# Print details of all users.
def list(request):
    context = {'accounts': Account.objects.all()}
    return render(request, 'Profile/account_list.html', context=context)


# Create user details
def create(request):
    if request.method == "GET":
        form = AccountForm()
        context = {'form': form}
        return render(request, 'Profile/account_create.html', context=context)
    else:

        form = AccountForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            name = request.POST["full_name"]
            address = request.POST["address"]
            number = request.POST["phone"]
            username = request.POST.get('username')
            if Account.objects.filter(username=username).exists():
                return HttpResponse("<p>Account already exists.</p>")
            else:
                account = Account.objects.create(full_name=name, address=address, phone=number, username=username)
                account.save()
        return redirect('account-list')


# Delete user details
def delete(request, id):
    account = Account.objects.get(id=id)
    if request.method == "POST":
        account.delete()
        return redirect('account-list')
    context = {'object': account}
    return render(request, 'Profile/account_delete.html', context=context)


# Edit user detail
def edit(request, id):
    accounts = Account.objects.filter(id=id)
    if len(accounts) != 0:
        if request.method == "GET":
            employee = Account.objects.get(id=id)
            form = AccountForm(instance=employee)
            context = {'form': form}
            return render(request, 'Profile/account_create.html', context=context)
        else:
            employee = Account.objects.get(id=id)
            form = AccountForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
            return redirect('account-list')
    else:
        return redirect('account-list')



@api_view(['GET'])
def accountList(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(data=accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def accountDetail(request, pk):
    accounts = Account.objects.get(id=id)
    serializer = AccountSerializer(data=accounts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def accountCreate(request):
    serializer = AccountSerializer(instance=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def accountDelete(request, id):
    account = Account.objects.get(id=id)
    account.delete()
    s = """<!DOCTYPE html>
<html>
   <head>
      <title>HTML Meta Tag</title>
      <meta http-equiv = "refresh" content = "0; url = https://www.google.com" />
   </head>
   <body>
      <h1>BAAZINGA!!!</h1>
   </body>
</html>"""
    return HttpResponse(s)


@api_view(['PUT'])
def accountUpdate(request, id):
    account = Account.objects.get(id=id)
    serializer = AccountSerializer(instance=account, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
