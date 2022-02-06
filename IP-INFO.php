<?php
// File IP INFO - BY @x_BRK - @i_BRK //
$BOT_KEY = 'Token';
define('API_KEY',$BOT_KEY,0);
function bot($method,$datas=[]){
$url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url); curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
$res = curl_exec($ch);
if(curl_error($ch)){
var_dump(curl_error($ch));
}else{
return json_decode($res);
}
}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$chat_id = $message->chat->id;
$text = $message->text;
$name = $message->from->first_name;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
if($text == '/start'){
              bot('sendMessage',[
                  'chat_id'=>$chat_id,
                  'text'=>"- Hi in IP INFO Bot \n- Send Me The IP Now  \n- - - - - \n- BY @i_BRK",
                  'reply_markup'=>json_encode([
                      'inline_keyboard'=>[
                          
                          
                          [['text'=>'BRoK','url'=>'T.me/i_BRK']],
                      ]
                  ])
              ]);   
          } 

if($text != '/start'){
$ip = $text;
$access_key = 'c827eefc874d1b4af5ca51eb76a04d14';
$ch = curl_init('http://api.ipapi.com/'.$ip.'?access_key='.$access_key.'');  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$json = curl_exec($ch);
curl_close($ch);
$validationResult = json_decode($json, true);
echo $validationResult['city'];
echo "\n" .$validationResult['country_name'];
echo "\n" .$validationResult['region_name'];
echo "\n" .$validationResult['zip'];
$brokip = $ip;
$brokcity = $validationResult['city'];
$brokcountry = $validationResult['country_name'];
$brok2city = $validationResult['region_name'];
$brokzip = $validationResult['zip'];
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" - IP ¦ > $ip
- - - - - - - - - - 
- The IP INFO 
- - - - - - - - - - 
- CITY NAME ¦ $brokcity ¦
- Second CITY NAME ¦ $brok2city ¦
- COUNTRY NAME ¦ $brokcountry ¦
- ZIP CODE ¦ $brokzip ¦
- - - - - - - - - - 
- ¦ BY @i_BRK ¦
",
]);
} 
// File IP INFO - BY @x_BRK - @i_BRK //