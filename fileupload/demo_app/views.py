
from django.shortcuts import render
from rest_framework import generics, status
import pandas as pd
from rest_framework.response import Response
from .models import File
from .serializers import FileUploadSerializer
from sqlalchemy.types import Integer,String
#import sqlalchemy
from sqlalchemy import create_engine



 

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        #df = pd.read_csv(file, dtype=str, nrows=100, header=None, encoding="unicode_escape")
 
    #     engine = create_engine('sqlite://', echo=False)
    #     engine.exec_driver_sql(
    #     "CREATE TEMPORARY TABLE temp_table AS SELECT * FROM main_table WHERE false"
    # )
    #     df.to_sql(name='File', con=engine, chunksize=1000, if_exists='replace', index=False)
        # df.to_sql('File', con=engine,  if_exists='append', index=False, chunksize=100)
       
        for index, row in reader.iterrows():
                        UniqueID=row["UniqueID (was Customer No.)"],
                        Company_name=row["Company name"],
                        Contact_person_Name=row['Contact person Name'],
                        Contact_phone=row["Contact phone"],
                        Contact_email=row["Contact email"],
                        Billing_rate_USD=row["Billing rate USD"],
                        Annual_increase_percentage=row["Annual increase percentage"],
                        Base_Pay_in_AUD=row["Base Pay in AUD"],
                        Company_address=row["Company address"]  

                        # print("".join(Contact_person_Name))
                        # print(int(''.join(map(str, UniqueID))))
                        # print(Company_name)
                        # print(Contact_person_Name)
                        # print(Contact_phone)
                        # print(Contact_email)
                        # print(Billing_rate_USD)
                        # print(Annual_increase_percentage)
                        # print(Base_Pay_in_AUD)
                        # print(Company_address)
                        # final=UniqueID+Company_name+Contact_person_Name+Contact_phone+Contact_email+Billing_rate_USD+Annual_increase_percentage+Base_Pay_in_AUD
                        # print(final)

                        File.objects.create(UniqueID=int(''.join(map(str, UniqueID))),
                                          Company_name="".join(Company_name),
                                          Contact_person_Name="".join(Contact_person_Name),
                                          Contact_phone=int(''.join(map(str, Contact_phone))),
                                          Contact_email=''.join(Contact_email),
                                          Billing_rate_USD=int(''.join(map(str, Billing_rate_USD))),
                                          Annual_increase_percentage=int(''.join(map(str, Annual_increase_percentage))),
                                          Base_Pay_in_AUD=int(''.join(map(str, Base_Pay_in_AUD))),
                                          Company_address=Company_address
                        )
                  

                
					
        return Response({"status": "success"}, status.HTTP_201_CREATED)
