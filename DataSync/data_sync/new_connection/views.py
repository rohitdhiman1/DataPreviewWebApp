from django.shortcuts import render,get_object_or_404, redirect
from django.forms import modelform_factory
import json,os,sys,csv
from .models import NewConnection
from .forms import NewConnectionForm

def new_connection_list(request):
    return render(request, "new_connection/connection_list.html", {"new_conn": NewConnection.objects.all()})

#New_Connection = modelform_factory(NewConnection, exclude=[])

def new(request):
    if request.method == "POST":
        form = NewConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            #converting the form response to a dictionary
            response_dict = form.data.dict()
            print(response_dict)
            print("Writing dictionary to json file")
            with open('form_HTTP_response.json', 'w') as outfile:
                json.dump(response_dict, outfile)
            return redirect("metadata_info")

    else:
        form = NewConnectionForm()
    return render(request, "new_connection/new.html", {"form": form})

def metadata_info(request):
    with open('form_HTTP_response.json') as f:
        metadata_dict = json.load(f)

    schema_name = metadata_dict['schema_name']
    table_name = metadata_dict['table_name']
    server_url = metadata_dict['server_url']
    port_number = metadata_dict['port_number']
    user_name = metadata_dict['user_name']
    password = metadata_dict['password']

    spark_submit_command_string = "spark-submit C:\\Users\\edhmrht\\Documents\\spark_code.py " + schema_name + " " +  table_name + " " + server_url + " " + port_number + " " + user_name + " " + password

    print(spark_submit_command_string)

    os.system(spark_submit_command_string)

    with open('C:\\Users\\edhmrht\\Documents\\MySBX\\DataSync\\data_sync\\metadata_info.json', 'r') as metadata_info_file:
        metadata_kv_pair_dict = json.load(metadata_info_file)

    return render(request, "new_connection/metadata_info.html",{"metadata_kv_pair_dict": metadata_kv_pair_dict})


def sample_data(request):
    with open('C:\\Users\\edhmrht\\Documents\\MySBX\\DataSync\\data_sync\\abc.json', 'r') as sample_records_file:
        sample_data_dict = json.load(sample_records_file)

    return render(request, "new_connection/sample_data.html", {"sample_data_dict": sample_data_dict})
