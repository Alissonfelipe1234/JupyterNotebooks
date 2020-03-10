<?php
require './vendor/autoload.php';
use Symfony\Component\DomCrawler\Crawler;

function cleanHead(String $value)
{
    return str_replace(" ", "_", $value);
}

$client = new GuzzleHttp\Client();

$response = $client->request('GET', 'http://guiatrabalhista.com.br/guia/salario_minimo.htm');
if (200 != $response->getStatusCode()) {
    echo "Error trying to connect: $response->getStatusCode()";
    exit;
}

unset($client);

$body = $response->getBody()->getContents();
$crawler = new Crawler($body);
$filter_content = '#content';
$content = $crawler
    ->filter($filter_content)
    ->each(function ($node) {
        return $node->html();
    });

unset($crawler);
$crawler = new Crawler($content);

$filter_table = 'tr td';
$table = $crawler->filter($filter_table)->each(function ($document) {return $document->text();});

unset($crawler);

$headers = array_splice($table, 0, 6);

$headers = array_map('cleanHead', $headers);

$data = array_chunk($table, 6);

$response = array();
foreach ($data as $arr) {
    $response[] = array_combine($headers, $arr);
}

// Aqui salvaria em um banco ou realizaria mais requisições

echo '<pre>';
print_r($response);
