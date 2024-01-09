from .models import Qcticket

def process_qc():
    queryset=Qcticket.objects.all()
    # get the query from the database with filter (process_flag and ticket status)
    queryset=queryset.filter(status="Completed").filter(qcresult="Has_Error").filter(mistaked_made_by__isnull=False)

    # if no result, then exit function
    if not queryset:
        # if queryset is nothing then return function
        return
    else:
        # loop the queryset
        for q in queryset:

            # get the country
            country = q.country.name
            
            # get role_1
            if q.role_1=="Actual":
                role_1_file_path=""
            elif q.role_1=="Shadow_1":
                role_1_file_path=""
            elif q.role_1=="Shadow_2":
                role_1_file_path=""
            elif q.role_1=="Shadow_3":
                role_1_file_path=""
            elif q.role_1=="Shadow_test":
                role_1_file_path=""
            
            # get role_2
            if q.role_2=="Actual":
                role_2_file_path=""
            elif q.role_2=="Shadow_1":
                role_2_file_path=""
            elif q.role_2=="Shadow_2":
                role_2_file_path=""
            elif q.role_2=="Shadow_3":
                role_2_file_path=""
            elif q.role_2=="Shadow_test":
                role_2_file_path=""

            # get qcfile
            qcfile=q.qcfile

            # sample of update field as below:
                # q.qcresult="No_Error"
                # q.save()
            
            
            # --------------------------------------
            # do something here on the qc file 
                # logging
                # set time outs!
                
                # try
                    # open read_excel role_1
                    # open read_excel role_2
                    # compare two df 
                    # if got variance then has error
                        # q.qcresult="Has_Error"
                    # elif no error
                        # q.qcresult="No_Error"
                    # update the necessary fields
                        # status = Completed
                        # process_flag = True
                # catch error
                    # status=script_error
                    # process_flag=true
            # --------------------------------------
 
            
            
            

        