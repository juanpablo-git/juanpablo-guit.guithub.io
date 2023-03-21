<?php
 include 'vendor/autoload.php';
// Parse PDF file and build necessary objects.
$parser = new \Smalot\PdfParser\Parser();
$pdf = $parser->parseFile('/var/www/leitorPDF/Leilaocaixa.pdf');

for ($i=1; $i < count($pdf->getPages()); $i++) { 
    $text = $pdf->getPages()[$i]->getDataTm();
    foreach($text as $key => $value) {
        $dadosLimpos[] = $value[1];
    }    
}
// echo "<pre>";
// print_r($dadosLimpos);
echo "<pre>";

for($i = 10; $i< 200; $i= $i+6) {

        if(strpos($dadosLimpos[$i+4],"R$") !== false) {

        
        
             $dadosRelacionados[$i]["lote"] = $dadosLimpos[$i];
             $dadosRelacionados[$i]["contrato"] = $dadosLimpos[$i+1];
             $dadosRelacionados[$i]["descricao"] = $dadosLimpos[$i+2] . $dadosLimpos[$i+3];
             $dadosRelacionados[$i]["valor"] = $dadosLimpos[$i+4];
             $i = $i+6;
        }else{

        $dadosRelacionados[$i]["lote"] = $dadosLimpos[$i];
        $dadosRelacionados[$i]["contrato"] = $dadosLimpos[$i+1];
        $dadosRelacionados[$i]["descricao"] = $dadosLimpos[$i+2] . $dadosLimpos[$i+3] . $dadosLimpos[$i+4];
        $dadosRelacionados[$i]["valor"] = $dadosLimpos[$i+5];
            

        }
        
    

   



    // break;
}
print_r( $dadosRelacionados);