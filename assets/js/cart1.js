document.getElementById('buy_out').style.display="none";
function myfunction(x,y,z,p){
                document.getElementById(x).style.display="";
                document.getElementById(y).style.display="none";
                var element = document.getElementById(z);
                element.classList.add("active");
                var elemen = document.getElementById(p);
                elemen.classList.remove("active");
            }