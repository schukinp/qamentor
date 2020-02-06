Use framework [selene](https://github.com/yashaka/selene) (python selenium wrapper)

# Precondition

* [Python 3.6+](https://www.python.org/)
* Browser [Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://chromedriver.chromium.org/)

Chrome is set up as default, but it is possible to change by `--browser` agrument to ie, firefox, safari 

Note: you need to have drivers for the above browsers in `PATH` 


# Installation

Install dependencies `pip3 install -r requirements.txt`

# Start tests

Linux example
```
$ pytest --browser chrome --base_url https://cwh-uat.bridgestonetire.com/
```

Same for Windows

# Test execution results

```
collected 5 items                                                                                                                                                                                                                                                          

tests\test_schedule_an_appointment.py
DevTools listening on ws://127.0.0.1:63481/devtools/browser/67e0059a-b577-4471-b827-fbdddc896851

Schedule An Appointment
 ✓ verify schedule appointment link on homepage
 ✓ cannot register without mandatory fields
 ✓ cannot register with existing email
 ✓ terms of use and privacy policy pages clickable
 ✓ create account success
                                                                                                                                                                                                                                                                     [100%]

=========================================================================================================================== 5 passed in 27.48s ============================================================================================================================
```