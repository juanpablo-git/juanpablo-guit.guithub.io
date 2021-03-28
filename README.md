    <html>
        <style>
            *{
                font-family: Lato Black;
            }
            body{
                background-color: darkcyan;
            }
            select{
                font-size: 10px;
            }
            #caixa{
                width: 500;
                height: 500;
                margin: 0 auto;
            font-size: 32px;    
            text-align: center;
            background-color: aquamarine ;
            box-shadow: 10px 5px 5px black;
            }
            #relogio{
               padding-top: 100px;
            }
            button{
                font-size: 20px;
                background-color: chartreuse;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
<div id="caixa">
    <div id="relogio">
        <label for="minuto">minuto</label>
        <select id="minuto" name="minuto"></select>
        <label for="segundo">segundo</label>
        <select id="segundo" name="segundo"></select>
       <br>
        <button  onclick="clicar()">iniciar</button>
    </div>

    <div id="tempo">
    </div>
</div>
    <script>
        var minuto = document.getElementById("minuto")
        var segundo = document.getElementById("segundo")
        var tempo = document.getElementById("tempo")
      for (let index = 0; index <=60; index++) {
         minuto.innerHTML +='<option value="'+index+'">'+index+'</option>'
         segundo.innerHTML +='<option value="'+index+'" >'+index+'</option>'
          
      }  

function clicar(){
    var seg = segundo.value
    var min = minuto.value
setInterval(function(){  
   
   
   if(seg<0){
       if(min==0){
           clearInterval(setInterval)
       }else{
           min--
           seg=59
       }
           
     
   }else{
      
   tempo.innerHTML=min+":"+seg
    seg-- 
}
   
  
    
    
},1000)


  
}

  
 

        
    </script>


    </html>




