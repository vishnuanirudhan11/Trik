
function myfunction(x,y,z,p){
    document.getElementById(x).style.display="none";
    document.getElementById(y).style.display="none";
    document.getElementById(z).style.display="none";
    document.getElementById(p).style.display="";
}

$(document).ready(function(){

    var date = new Date()
    var month = date.getMonth()+1
    var year = date.getFullYear()
    localStorage.setItem("key", 1);

    var  url = 'http://127.0.0.1:8000/adminhome/api/rest/'+year;
    var defaul=[]
    var label=[]

    document.getElementById('tab2').style.display="none";
    document.getElementById('tab3').style.display="none";
    document.getElementById('tab4').style.display="none";
    document.getElementById('det2').style.display="none";
    document.getElementById('msg2').style.display="none";




loadHtml()
fun(url)
    })

function loadHtml(){
    fetch('http://127.0.0.1:8000/adminhome/htmlfile/')
    .then((response)=> response.text())
    .then((html)=> document.getElementById('load_html').innerHTML = html);
}

async function fun(url){
    const response = await fetch(url);
    const data = await response.json();
    var {label,defaul,total,cat_name,cat_income,sold_items,itemcount,user_joind,views,cancel_frequency} = data;

//chart1
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: defaul,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
//chart2


 var ctx = document.getElementById('income').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: cat_name,
        datasets: [{
            label: '# of Votes',
            data: cat_income,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


//chart3


 var ctx = document.getElementById('items_sold').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: sold_items,
        datasets: [{
            label: '# of Votes',
            data: itemcount,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

//chart4

 var ctx = document.getElementById('acc_created').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: user_joind,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


//chart5


 var ctx = document.getElementById('performance').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: views,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

//chart 6

 var ctx = document.getElementById('cancel').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: cancel_frequency,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    responsive:false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


}


function chartfun(x,y){
    var date = new Date()
    var month = date.getMonth()+1
    var year = date.getFullYear()
    var list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'August', 'september', 'october','novamber','december']
    var i = localStorage.getItem("key");
    if (i == 1){i = year}

    if (y == null){
        var  base_url = 'http://127.0.0.1:8000/adminhome/api/rest/'
        url=base_url + x ;
        document.getElementById('btn2').innerText = 'jan-dec';
        localStorage.setItem("key",x);
        i = localStorage.getItem("key");

    }else{
    var  base_url = 'http://127.0.0.1:8000/adminhome/api/rest/'
    url=base_url + i + '/' + y;
    document.getElementById('btn2').innerText = list[y-1];
    }
    document.getElementById('btn1').innerText = i;


    loadHtml()
    fun(url)

}

function clietDetail(id){
    fetch('http://127.0.0.1:8000/adminhome/detail/'+id)
    .then((response)=> response.text())
    .then((html)=> document.getElementById('detail').innerHTML = html);
}

function msg_detail(id){
    fetch('http://127.0.0.1:8000/adminhome/msg_detail/'+id)
    .then((response)=> response.text())
    .then((html)=> document.getElementById('messages').innerHTML = html);
}

function msg_action(id,act){
    fetch('http://127.0.0.1:8000/adminhome/msg_detail/'+id+'/'+act)
    .then((response)=> response.text())
    .then((html)=> document.getElementById('messages').innerHTML = html);
}



function ord_process(id,prs){
    fetch('http://127.0.0.1:8000/adminhome/ord_process/'+id+'/'+prs)
    .then((response)=> response.text())
    .then((html)=> document.getElementById('detail').innerHTML = html);

}

function post_deliver(id){
    fetch('http://127.0.0.1:8000/adminhome/post_details/'+id)
    .then((response)=> response.text())
    .then((html)=> document.getElementById('post_deliver').innerHTML = html);

}


function msgfun(x,y,z,p){
                document.getElementById(x).style.display="";
                document.getElementById(y).style.display="none";
                var element = document.getElementById(z);
                element.classList.add("active");
                var elemen = document.getElementById(p);
                elemen.classList.remove("active");
           }


function detail_nav(x,y,z,p){
                document.getElementById(x).style.display="";
                document.getElementById(y).style.display="none";
                var element = document.getElementById(z);
                element.classList.add("active");
                var elemen = document.getElementById(p);
                elemen.classList.remove("active");
            }
