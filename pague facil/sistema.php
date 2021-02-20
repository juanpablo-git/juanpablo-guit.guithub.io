
 <!DOCTYPE html>
 <html>
 <meta charset="utf-8">
 <head>
 	<title>sistema pague facil</title>
 

 <style type="text/css">
 	
*{
	font-size: 20px;
	font-family:  arial;
}
 	
 	#Rdados{
 		margin-left: 40%;	
 	}
 	button{
 		margin-top: 20px;
 	}
 	table{
 		margin-top: 20px;
 	}
 </style>
 </head>
<body background="papel.jpg">
 <CENTER><h1>PÁGINA DE PAGAMENTO</h1></CENTER>
<div id="Rdados">
 
 <form action="sistema.php" method="GET">
 	<label>valor da conta</label>
 	<input type="number" name="valorR"><br>
 	<label>tipo de pagamento</label>	
	<img src="download (1).jpg" width="30" height="30"> <input type="radio" name="Pcartão" value="1">cartão
	<img src="download.jpg" width="30" height="30"> <input type="radio" name="Pavista" value="0" >avista
	<BR>
	<button>enviar</button>
</form>


<?php
$valorConta=isset($_GET["valorR"])?$_GET["valorR"]:null;
$tipoPagamento=isset( $_GET["Pcartão"] )?$_GET["Pcartão"]:null;
?>

<table border="2">
	<tr>
		<td>valor(R$)</td> <td>Taxa cartão</td> <td>Valor Total</td>
	</tr>
	<tr>
		<td>
			<?php echo $valorConta;  ?>
		</td>
		<td>
		<?php

switch ($tipoPagamento) {
	case 0:
		$tipoPagamento=$tipoPagamento*0;
		echo $tipoPagamento;
		break;
	
	case 1:
		$tipoPagamento=$valorConta*0.05;
		echo $tipoPagamento;
		break;
		
}


?>
</td>
	<td>
		<?php echo $tipoPagamento+$valorConta; ?>
	</td>	
</tr>
</table>
</div>
