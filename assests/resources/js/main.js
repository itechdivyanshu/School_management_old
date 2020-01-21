//for date:
        function renderTime(){
            var mydate = new Date();
            var year = mydate.getYear();
                if (year < 1000){
                    year+=1900;
                }
            var day = mydate.getDay();
            var daym = mydate.getDate();
            var dayarray = new Array("Sunday","Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday");
        
        //date end
        
        //for time:
        var currentTime = new Date();
        var h = currentTime.getHours();
        var m = currentTime.getMinutes();
            if (h==24){
                h=0;
            }else if(h>12){
                h = h-0;
            }
            if (h<10){
                h="0"+h;
            }
            if (m<10){
                m = "0"+m;
            }
            
        var myclock = document.getElementById("date");
        myclock.textContent = "" + dayarray[day]+" "+daym+" | "+h+":"+m;
        myclock.innerHTML = "" + dayarray[day]+" "+daym+" | "+h+":"+m;
            
        setTimeout("renderTime()",1000);
        }
        renderTime();






















