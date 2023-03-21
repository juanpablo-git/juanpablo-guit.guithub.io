<?php
include 'vendor/autoload.php';
// Parse PDF file and build necessary objects.
$parser = new \Smalot\PdfParser\Parser();
$pdf = $parser->parseFile('/var/www/leitorPDF/Leilaocaixa.pdf');

$descricao = "";
$lote = [];
$posicao = 0;
for ($i=1; $i < count($pdf->getPages()); $i++) { 
    $text = $pdf->getPages()[$i]->getDataTm();
    foreach($text as $key => $value) {
        $dadosLimpos[] = $value[1];
    }    

for($indice = $posicao+10; $indice< count($dadosLimpos); $indice++) {
  
    if($dadosLimpos[$indice] == "UNIDADES PARTICIPANTES:"){
        break;
    }
    if(strpos($dadosLimpos[$indice],"R$") !== FALSE){
        $relacionamento[$indice]["lote"] = $lote[0]."/".$lote[1];
        $relacionamento[$indice]["descricao"] = $descricao;
        $relacionamento[$indice]["valor"] =  $dadosLimpos[$indice];
        $lote = [];
        $descricao = "";
        $posicao = $indice+1;
        continue;

    }
    if((strpos($dadosLimpos[$indice],"-") !== FALSE) && (strpos($dadosLimpos[$indice],".") !== FALSE)){
        $lote[] = $dadosLimpos[$indice];
        continue;
    }

    $descricao .= $dadosLimpos[$indice]."\n";

      
            
}

}

$cabecalho = ["lote","descricao","valor"];
$arquivo = fopen("/var/www/teste.csv","w");
fputcsv($arquivo,$cabecalho,";");

foreach($relacionamento as $relacionamento){
    fputcsv($arquivo,$relacionamento,";");
}

fclose($arquivo);

// echo "<pre>";
// echo $descricao;
// print_r( $relacionamento);
