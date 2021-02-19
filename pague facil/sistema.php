
 <!DOCTYPE html>
 <html>
 <meta charset="utf-8">
 <head>
 	<title></title>
 	<style type="text/css">
 		form{
 			

 			font-size: 30px;
 			font-family:arial;
 		}
 		input{
 			margin-right: -50PX;
 			margin-left: 20PX;
 			width: 150px;
 			height: 30px;
 		}
 		input.raio{
 			margin-left: -40px;
 			
 		}
 		h3{
 			text-align: center;
 			font-family:Candara;
 		}
 		table{
 			margin: auto;
 			text-align: center;
 			font-size: 30px;
 			font-family: arial;
 		}
 		fieldset{
 			position: relative;
 			margin-top: 25%;
 		}
 		
 	</style>
 </head>
 <body background="papel.jpg">
 
 
 <form action="sistema.php" method="GET">
 <label> valor total da conta</label><input type="numer"  name="num">
 <br>
<label> tipo de pagamento</label>

<input class="raio" type="radio" name="analizar" value="5/100"><img src="download (1).jpg" width="100" height="100">cartão
<input class="raio" type="radio" name="analizar" value="0"><img src="download.jpg" width="100" height="100">avista


</form>
<?php

$valorConta=$_GET["num"];
$tipoPagamento=isset($_GET["analizar"])?$_GET["analizar"]:0;
$acrescimoSistema=(((5/100)*$valorConta)+$valorConta);
$acrescimoCartao=(($acrescimoSistema*$pagamentoCartao)/100)+$acrescimoSistema;
$total=$acrescimoCartao;
?>

<fieldset>


<table border="black">
	<tr><td>valor da conta</td><td>acrescimo de 5% do sistema</td><td>com acrescimo de 5% do cartão</td><td><?php echo "valor total"; ?></td></tr>
	<tr><td><?php echo "$valorConta"; ?></td><td><?php echo "$acrescimoSistema";  ?></td><td><?php echo "$acrescimoCartao"; ?></td><td><?php echo "$total";  ?></td></tr>
	
	
</table>
</fieldset>
	
</body>
</html>

