- `crontab -l` : `Show all the running scripts`
- `crontab -e` : `Open crontab for editing mode`
    - This will open crontab in vim editor

- Press I to enter the insert/edit mode
	- To save press escape
	- To quit `-->` `:wq`


- `sudo service cron reload` : `To restart cron`

Sample Script: 

- ```*/2 * * * *  /usr/bin/env bash -c 'source /home/hv778899/projects/DBT_Backend/dbtenv/bin/activate && cd  /home/hv778899/projects/DBT_Backend/dbt_backend && python3 manage.py runcrons schedulers.programs.applicant_initial_sms'>/dev/null 2 >> new_file_logs.txt```
<br>
    
  - Explanation:
    - Activate the virtual environment
    - Go to django main repository
    - run the following command
     
    - `python3 manage.py runcrons schedulers.programs.applicant_initial_sms'>/dev/null 2`

To get the output of the sceduler:

   - `python3 manage.py runcrons schedulers.programs.applicant_initial_sms'>/dev/null 2 >>output_logs.txt`


Link: https://crontab.guru/

______

__NOTES:__

`export EDITOR=vim` : `To set default editor`
eg. nano to vim

_______

```
from django_cron import CronJobBase, Schedule
```
```
class TestFunc(CronJobBase):
    GAP_MIN = 2
    schedule = Schedule(run_every_mins=GAP_MIN)
    code = 'TestFunc,'
    
    def do(self):
        print('help')
        return True
```
```
class applicant_initial_sms(CronJobBase):
    GAP_MIN = 2
    schedule = Schedule(run_every_mins=GAP_MIN)
    code = 'applicant_initial_sms,'

    def do(self):
        type = models.NotifyType.objects.get(type = 'Initial')
        new_applications = ApplicantLifeCycle.objects.filter(is_active = True).filter(initial_sms = False)
        for application in new_applications:
            scheme = application.scheme.scheme_name
            app_num = application.application_no
            mobile_num = application.mobile_num
            tempid = 1007224187689323772
            entityid = 1001629542890983159
            domain = 'https://socialtick.club:8002/'
            url = 'id/{uuid}'.format(uuid=application.sid)
            sms_text = 'Dear Applicant,\r\n\r\nThe verification is initiated under {service}. Your application number is {app_num}\r\n\r\nPlease click on the below link to proceed.\r\n{domain}{url}\r\n\r\nTeam Helloverify'.format(service=scheme,app_num=app_num,domain=domain,url=url)
            r = requests.post(f"http://103.16.101.52:8080/sendsms/bulksms?username=oz07-hellovrfy&password=68HuHty2&type=0&dlr=1&destination={mobile_num}&source=HLVRFY&message={sms_text}&entityid={entityid}&tempid={tempid}")
            
            if r.status_code == 200:
                application.initial_sms = True
                application.sms_sent_time = datetime.now()
                application.save()
            
            models.SMSLogs.objects.create(
                applicant = application,
                notify_type = type,
                content = sms_text,
                mobile = mobile_num,
                response_text = r.text,
                response_code = r.status_code
            )   
            
            return True

```

