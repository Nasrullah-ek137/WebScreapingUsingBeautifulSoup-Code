{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b7db96f1-cef7-4d8b-b92c-7beb290c29c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests as re\n",
    "from bs4 import BeautifulSoup\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4cceb3b3-cc96-4525-bbf1-7c542942a2c3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<html itemscope=\"\" itemtype=\"http://schema.org/WebPage\" lang=\"en-IN\">\n",
      " <head>\n",
      "  <meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/>\n",
      "  <meta content=\"/images/branding/googleg/1x/googleg_standard_color_128dp.png\" itemprop=\"image\"/>\n",
      "  <title>\n",
      "   Google\n",
      "  </title>\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){var _g={kEI:'W0vHZrPnNMHc2roP4PbV-Q4',kEXPI:'0,3700337,612,432,8,89,541439,2891,89155,18161,145698,2,16737,23024,6700,41948,54821,2913,2,2,1,26632,8155,8860,14490,8702,13734,9779,62657,33565,42644,15816,1804,7734,27535,13448,9708,13154,6414,11106,15977,5212676,998,145,5991287,2840645,688,14,51,34,1,15,4,9,2,5,1,1,1,14,2,3,1,1,2,8,3,1,8,6,1,8,3,4,3,3,3,5,1,6,1,3,5,1,2,1,7440626,20556611,43887,3,318,4,1281,3,2124363,23029351,6870,2,1291,10336,10736,84045,11523,11099,15165,8182,149,10657,9908,28715,5969,3960,11746,6749,155,2,2482,13503,7736,9139,4600,328,3217,4,3004,6760,3658,3549,5706,410,518,3765,1954,1670,5634,687,2730,2,3944,1119,3,5,3010,2695,2757,1718,1643,252,4192,5784,682,451,122,4,87,7184,6519,1489,418,3,302,2,9,3997,3,5,2704,161,1,2,1694,294,405,8,4134,2379,448,118,918,795,185,308,221,2767,3792,1,6,2281,3340,4,251,1575,8526,501,1963,134,4,561,98,378,74,1940,245,4979,607,4,1001,2,1531,565,710,58,441,126,496,167,204,651,895,677,387,732,4,109,2,10552,1183,660,566,1010,2,5,2,465,251,84,203,2,3,493,7,1111,160,31,1526,7,168,158,20,1337,3,569,52,2691,2,614,1170,605,943,20,360,20,251,284,92,10,8,1,39,317,122,1,347,527,98,1,26,4,13,4,582,306,4,109,608,637,3,38,116,293,1151,82,124,21,215,4,5,432,323,90,109,434,896,341,3,198,326,85,33,60,95,380,15,1448,2,2,2,3,526,935,38,3,280,818,5,9,39,775,4,2,3,178,1,8,1,1,4,1,4,554,112,244,3,1407,1090,24,568,504,192,13,1484,1655,21126404,365636,3,14475,3,2927,4126,1112,47',kBL:'rDiN',kOPI:89978449};(function(){var a;((a=window.google)==null?0:a.stvsc)?google.kEI=_g.kEI:window.google=_g;}).call(this);})();(function(){google.sn='webhp';google.kHL='en-IN';})();(function(){\n",
      "var h=this||self;function l(){return window.google!==void 0&&window.google.kOPI!==void 0&&window.google.kOPI!==0?window.google.kOPI:null};var m,n=[];function p(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute(\"eid\")));)a=a.parentNode;return b||m}function q(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute(\"leid\")));)a=a.parentNode;return b}function r(a){/^http:/i.test(a)&&window.location.protocol===\"https:\"&&(google.ml&&google.ml(Error(\"a\"),!1,{src:a,glmm:1}),a=\"\");return a}\n",
      "function t(a,b,c,d,k){var e=\"\";b.search(\"&ei=\")===-1&&(e=\"&ei=\"+p(d),b.search(\"&lei=\")===-1&&(d=q(d))&&(e+=\"&lei=\"+d));d=\"\";var g=b.search(\"&cshid=\")===-1&&a!==\"slh\",f=[];f.push([\"zx\",Date.now().toString()]);h._cshid&&g&&f.push([\"cshid\",h._cshid]);c=c();c!=null&&f.push([\"opi\",c.toString()]);for(c=0;c<f.length;c++){if(c===0||c>0)d+=\"&\";d+=f[c][0]+\"=\"+f[c][1]}return\"/\"+(k||\"gen_204\")+\"?atyp=i&ct=\"+String(a)+\"&cad=\"+(b+e+d)};m=google.kEI;google.getEI=p;google.getLEI=q;google.ml=function(){return null};google.log=function(a,b,c,d,k,e){e=e===void 0?l:e;c||(c=t(a,b,e,d,k));if(c=r(c)){a=new Image;var g=n.length;n[g]=a;a.onerror=a.onload=a.onabort=function(){delete n[g]};a.src=c}};google.logUrl=function(a,b){b=b===void 0?l:b;return t(\"\",a,b)};}).call(this);(function(){google.y={};google.sy=[];var d;(d=google).x||(d.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1});var e;(e=google).sx||(e.sx=function(a){google.sy.push(a)});google.lm=[];var f;(f=google).plm||(f.plm=function(a){google.lm.push.apply(google.lm,a)});google.lq=[];var g;(g=google).load||(g.load=function(a,b,c){google.lq.push([[a],b,c])});var h;(h=google).loadAll||(h.loadAll=function(a,b){google.lq.push([a,b])});google.bx=!1;var k;(k=google).lx||(k.lx=function(){});var l=[],m;(m=google).fce||(m.fce=function(a,b,c,n){l.push([a,b,c,n])});google.qce=l;}).call(this);google.f={};(function(){\n",
      "document.documentElement.addEventListener(\"submit\",function(b){var a;if(a=b.target){var c=a.getAttribute(\"data-submitfalse\");a=c===\"1\"||c===\"q\"&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener(\"click\",function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if(a.tagName===\"A\"){a=a.getAttribute(\"data-nohref\")===\"1\";break a}a=!1}a&&b.preventDefault()},!0);}).call(this);\n",
      "  </script>\n",
      "  <style>\n",
      "   #gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n",
      "  </style>\n",
      "  <style>\n",
      "   body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1967d2}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#681da8;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#1967d2}a:visited{color:#681da8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;color:#000;border:none;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:focus{outline:none}\n",
      "  </style>\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){window.google.erd={jsr:1,bv:2066,de:true};\n",
      "var g=this||self;var k,l=(k=g.mei)!=null?k:1,n,p=(n=g.sdo)!=null?n:!0,q=0,r,t=google.erd,v=t.jsr;google.ml=function(a,b,d,m,e){e=e===void 0?2:e;b&&(r=a&&a.message);d===void 0&&(d={});d.cad=\"ple_\"+google.ple+\".aple_\"+google.aple;if(google.dl)return google.dl(a,e,d,!0),null;b=d;if(v<0){window.console&&console.error(a,b);if(v===-2)throw a;b=!1}else b=!a||!a.message||a.message===\"Error loading script\"||q>=l&&!m?!1:!0;if(!b)return null;q++;d=d||{};b=encodeURIComponent;var c=\"/gen_204?atyp=i&ei=\"+b(google.kEI);google.kEXPI&&(c+=\"&jexpid=\"+b(google.kEXPI));c+=\"&srcpg=\"+b(google.sn)+\"&jsr=\"+b(t.jsr)+\n",
      "\"&bver=\"+b(t.bv);t.dpf&&(c+=\"&dpf=\"+b(t.dpf));var f=a.lineNumber;f!==void 0&&(c+=\"&line=\"+f);var h=a.fileName;h&&(h.indexOf(\"-extension:/\")>0&&(e=3),c+=\"&script=\"+b(h),f&&h===window.location.href&&(f=document.documentElement.outerHTML.split(\"\\n\")[f],c+=\"&cad=\"+b(f?f.substring(0,300):\"No script found.\")));google.ple&&google.ple===1&&(e=2);c+=\"&jsel=\"+e;for(var u in d)c+=\"&\",c+=b(u),c+=\"=\",c+=b(d[u]);c=c+\"&emsg=\"+b(a.name+\": \"+a.message);c=c+\"&jsst=\"+b(a.stack||\"N/A\");c.length>=12288&&(c=c.substr(0,12288));a=c;m||google.log(0,\"\",a);return a};window.onerror=function(a,b,d,m,e){r!==a&&(a=e instanceof Error?e:Error(a),d===void 0||\"lineNumber\"in a||(a.lineNumber=d),b===void 0||\"fileName\"in a||(a.fileName=b),google.ml(a,!1,void 0,!1,a.name===\"SyntaxError\"||a.message.substring(0,11)===\"SyntaxError\"||a.message.indexOf(\"Script error\")!==-1?3:0));r=null;p&&q>=l&&(window.onerror=null)};})();\n",
      "  </script>\n",
      " </head>\n",
      " <body bgcolor=\"#fff\">\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\n",
      "if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n",
      "}\n",
      "})();\n",
      "  </script>\n",
      "  <div id=\"mngb\">\n",
      "   <div id=\"gbar\">\n",
      "    <nobr>\n",
      "     <b class=\"gb1\">\n",
      "      Search\n",
      "     </b>\n",
      "     <a class=\"gb1\" href=\"https://www.google.com/imghp?hl=en&amp;tab=wi\">\n",
      "      Images\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://maps.google.co.in/maps?hl=en&amp;tab=wl\">\n",
      "      Maps\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://play.google.com/?hl=en&amp;tab=w8\">\n",
      "      Play\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://www.youtube.com/?tab=w1\">\n",
      "      YouTube\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://news.google.com/?tab=wn\">\n",
      "      News\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://mail.google.com/mail/?tab=wm\">\n",
      "      Gmail\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://drive.google.com/?tab=wo\">\n",
      "      Drive\n",
      "     </a>\n",
      "     <a class=\"gb1\" href=\"https://www.google.co.in/intl/en/about/products?tab=wh\" style=\"text-decoration:none\">\n",
      "      <u>\n",
      "       More\n",
      "      </u>\n",
      "      »\n",
      "     </a>\n",
      "    </nobr>\n",
      "   </div>\n",
      "   <div id=\"guser\" width=\"100%\">\n",
      "    <nobr>\n",
      "     <span class=\"gbi\" id=\"gbn\">\n",
      "     </span>\n",
      "     <span class=\"gbf\" id=\"gbf\">\n",
      "     </span>\n",
      "     <span id=\"gbe\">\n",
      "     </span>\n",
      "     <a class=\"gb4\" href=\"http://www.google.co.in/history/optout?hl=en\">\n",
      "      Web History\n",
      "     </a>\n",
      "     |\n",
      "     <a class=\"gb4\" href=\"/preferences?hl=en\">\n",
      "      Settings\n",
      "     </a>\n",
      "     |\n",
      "     <a class=\"gb4\" href=\"https://accounts.google.com/ServiceLogin?hl=en&amp;passive=true&amp;continue=https://www.google.com/&amp;ec=GAZAAQ\" id=\"gb_70\" target=\"_top\">\n",
      "      Sign in\n",
      "     </a>\n",
      "    </nobr>\n",
      "   </div>\n",
      "   <div class=\"gbh\" style=\"left:0\">\n",
      "   </div>\n",
      "   <div class=\"gbh\" style=\"right:0\">\n",
      "   </div>\n",
      "  </div>\n",
      "  <center>\n",
      "   <br clear=\"all\" id=\"lgpd\"/>\n",
      "   <div id=\"XjhHGf\">\n",
      "    <img alt=\"Google\" height=\"92\" id=\"hplogo\" src=\"/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png\" style=\"padding:28px 0 14px\" width=\"272\"/>\n",
      "    <br/>\n",
      "    <br/>\n",
      "   </div>\n",
      "   <form action=\"/search\" name=\"f\">\n",
      "    <table cellpadding=\"0\" cellspacing=\"0\">\n",
      "     <tr valign=\"top\">\n",
      "      <td width=\"25%\">\n",
      "      </td>\n",
      "      <td align=\"center\" nowrap=\"\">\n",
      "       <input name=\"ie\" type=\"hidden\" value=\"ISO-8859-1\"/>\n",
      "       <input name=\"hl\" type=\"hidden\" value=\"en-IN\"/>\n",
      "       <input name=\"source\" type=\"hidden\" value=\"hp\"/>\n",
      "       <input name=\"biw\" type=\"hidden\"/>\n",
      "       <input name=\"bih\" type=\"hidden\"/>\n",
      "       <div class=\"ds\" style=\"height:32px;margin:4px 0\">\n",
      "        <input autocomplete=\"off\" class=\"lst\" maxlength=\"2048\" name=\"q\" size=\"57\" style=\"margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000\" title=\"Google Search\" value=\"\"/>\n",
      "       </div>\n",
      "       <br style=\"line-height:0\"/>\n",
      "       <span class=\"ds\">\n",
      "        <span class=\"lsbb\">\n",
      "         <input class=\"lsb\" name=\"btnG\" type=\"submit\" value=\"Google Search\"/>\n",
      "        </span>\n",
      "       </span>\n",
      "       <span class=\"ds\">\n",
      "        <span class=\"lsbb\">\n",
      "         <input class=\"lsb\" id=\"tsuid_1\" name=\"btnI\" type=\"submit\" value=\"I'm Feeling Lucky\"/>\n",
      "         <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "          (function(){var id='tsuid_1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\n",
      "else top.location='/doodles/';};})();\n",
      "         </script>\n",
      "         <input name=\"iflsig\" type=\"hidden\" value=\"AL9hbdgAAAAAZsdZa4ziFtqK3Fb8bo_UejnhlIlRJz7M\"/>\n",
      "        </span>\n",
      "       </span>\n",
      "      </td>\n",
      "      <td align=\"left\" class=\"fl sblc\" nowrap=\"\" width=\"25%\">\n",
      "       <a href=\"/advanced_search?hl=en-IN&amp;authuser=0\">\n",
      "        Advanced search\n",
      "       </a>\n",
      "      </td>\n",
      "     </tr>\n",
      "    </table>\n",
      "    <input id=\"gbv\" name=\"gbv\" type=\"hidden\" value=\"1\"/>\n",
      "    <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "     (function(){var a,b=\"1\";if(document&&document.getElementById)if(typeof XMLHttpRequest!=\"undefined\")b=\"2\";else if(typeof ActiveXObject!=\"undefined\"){var c,d,e=[\"MSXML2.XMLHTTP.6.0\",\"MSXML2.XMLHTTP.3.0\",\"MSXML2.XMLHTTP\",\"Microsoft.XMLHTTP\"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b=\"2\"}catch(h){}}a=b;if(a==\"2\"&&location.search.indexOf(\"&gbv=2\")==-1){var f=google.gbvu,g=document.getElementById(\"gbv\");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);\n",
      "    </script>\n",
      "   </form>\n",
      "   <div style=\"font-size:83%;min-height:3.5em\">\n",
      "    <br/>\n",
      "    <div id=\"gws-output-pages-elements-homepage_additional_languages__als\">\n",
      "     <style>\n",
      "      #gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{color:#474747;display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}\n",
      "     </style>\n",
      "     <div id=\"SIvCob\">\n",
      "      Google offered in:\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=hi&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAY\">\n",
      "       हिन्दी\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=bn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAc\">\n",
      "       বাংলা\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=te&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAg\">\n",
      "       తెలుగు\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=mr&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAk\">\n",
      "       मराठी\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=ta&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAo\">\n",
      "       தமிழ்\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=gu&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAs\">\n",
      "       ગુજરાતી\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=kn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCAw\">\n",
      "       ಕನ್ನಡ\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=ml&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCA0\">\n",
      "       മലയാളം\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefs?sig=0_M35cn6iv-7SZGgbe0DbbK5OH8mM%3D&amp;hl=pa&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjzgIrt54iIAxVBrlYBHWB7Ne8Q2ZgBCA4\">\n",
      "       ਪੰਜਾਬੀ\n",
      "      </a>\n",
      "     </div>\n",
      "    </div>\n",
      "   </div>\n",
      "   <span id=\"footer\">\n",
      "    <div style=\"font-size:10pt\">\n",
      "     <div id=\"WqQANb\" style=\"margin:19px auto;text-align:center\">\n",
      "      <a href=\"/intl/en/ads/\">\n",
      "       Advertising\n",
      "      </a>\n",
      "      <a href=\"http://www.google.co.in/services/\">\n",
      "       Business Solutions\n",
      "      </a>\n",
      "      <a href=\"/intl/en/about.html\">\n",
      "       About Google\n",
      "      </a>\n",
      "      <a href=\"https://www.google.com/setprefdomain?prefdom=IN&amp;prev=https://www.google.co.in/&amp;sig=K_3FpZuxPHzT0lbkxEQwGb6jDiD-I%3D\">\n",
      "       Google.co.in\n",
      "      </a>\n",
      "     </div>\n",
      "    </div>\n",
      "    <p style=\"font-size:8pt;color:#70757a\">\n",
      "     © 2024 -\n",
      "     <a href=\"/intl/en/policies/privacy/\">\n",
      "      Privacy\n",
      "     </a>\n",
      "     -\n",
      "     <a href=\"/intl/en/policies/terms/\">\n",
      "      Terms\n",
      "     </a>\n",
      "    </p>\n",
      "   </span>\n",
      "  </center>\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){window.google.cdo={height:757,width:1440};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d=c.compatMode==\"CSS1Compat\"?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}\n",
      "if(a&&b&&(a!=google.cdo.width||b!=google.cdo.height)){var e=google,f=e.log,g=\"/client_204?&atyp=i&biw=\"+a+\"&bih=\"+b+\"&ei=\"+google.kEI,h=\"\",k=[],l=window.google!==void 0&&window.google.kOPI!==void 0&&window.google.kOPI!==0?window.google.kOPI:null;l!=null&&k.push([\"opi\",l.toString()]);for(var m=0;m<k.length;m++){if(m===0||m>0)h+=\"&\";h+=k[m][0]+\"=\"+k[m][1]}f.call(e,\"\",\"\",g+h)};}).call(this);})();\n",
      "  </script>\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){google.xjs={basecomb:'/xjs/_/js/k\\x3dxjs.hp.en.Fjn4nALTu_Q.O/ck\\x3dxjs.hp.5zRekhoQe3I.L.X.O/am\\x3dAQAAABAAAAAAAAAAAAAAAAAAAAAAAAAAIAQAAAAAAAAQAAaAAwAAQACAgAAAAAAA8AAAAAAAAIAAhAAAKAAIEAAciO8IAATAIgAAvA/d\\x3d1/ed\\x3d1/dg\\x3d0/ujg\\x3d1/rs\\x3dACT90oEK2KgMrcUwr10qXhni17XOPR5WMA',basecss:'/xjs/_/ss/k\\x3dxjs.hp.5zRekhoQe3I.L.X.O/am\\x3dAQAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAQAAAAAAAAQACAgAAAAAAAAAAAAAAAAIAAhAAAKAAIEA/rs\\x3dACT90oF0YGB4KqZwyysvB7EUH2AHKCTxPw',basejs:'/xjs/_/js/k\\x3dxjs.hp.en.Fjn4nALTu_Q.O/am\\x3dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAaAAwAAAAAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAciO8IAATAIgAAvA/dg\\x3d0/rs\\x3dACT90oEFArDapCzScN--oG2HOGDOQclU8g',excm:[]};})();\n",
      "  </script>\n",
      "  <link href=\"/xjs/_/ss/k=xjs.hp.5zRekhoQe3I.L.X.O/am=AQAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAQAAAAAAAAQACAgAAAAAAAAAAAAAAAAIAAhAAAKAAIEA/d=1/ed=1/rs=ACT90oF0YGB4KqZwyysvB7EUH2AHKCTxPw/m=sb_he,d\" nonce=\"GlEisf-diC8KV7qW5kgEXA\" rel=\"stylesheet\"/>\n",
      "  <script nonce=\"GlEisf-diC8KV7qW5kgEXA\">\n",
      "   (function(){var u='/xjs/_/js/k\\x3dxjs.hp.en.Fjn4nALTu_Q.O/am\\x3dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAaAAwAAAAAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAciO8IAATAIgAAvA/d\\x3d1/ed\\x3d1/dg\\x3d3/rs\\x3dACT90oEFArDapCzScN--oG2HOGDOQclU8g/m\\x3dsb_he,d';var st=1;var amd=1000;var mmd=0;var pod=true;\n",
      "var f=this||self,g=function(a){return a};var h;var k={},l=function(a){this.g=a};l.prototype.toString=function(){return this.g+\"\"};var m=function(a){return a instanceof l&&a.constructor===l?a.g:\"type_error:TrustedResourceUrl\"};\n",
      "var n=/^\\s*(?!javascript:)(?:[\\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var p=\"alternate author bookmark canonical cite help icon license modulepreload next prefetch dns-prefetch prerender preconnect preload prev search subresource\".split(\" \");function q(a,b){a.src=m(b);var c,d;(c=(b=(d=(c=(a.ownerDocument&&a.ownerDocument.defaultView||window).document).querySelector)==null?void 0:d.call(c,\"script[nonce]\"))?b.nonce||b.getAttribute(\"nonce\")||\"\":\"\")&&a.setAttribute(\"nonce\",c)};var r=function(a){var b=document;a=String(a);b.contentType===\"application/xhtml+xml\"&&(a=a.toLowerCase());return b.createElement(a)};function t(a){a=a===null?\"null\":a===void 0?\"undefined\":a;if(h===void 0){var b=null;var c=f.trustedTypes;if(c&&c.createPolicy){try{b=c.createPolicy(\"goog#html\",{createHTML:g,createScript:g,createScriptURL:g})}catch(d){f.console&&f.console.error(d.message)}h=b}else h=b}a=(b=h)?b.createScriptURL(a):a;return new l(a,k)};google.ps===void 0&&(google.ps=[]);function w(){var a=u,b=function(){};google.lx=google.stvsc?b:function(){x(a);google.lx=b};google.bx||google.lx()}function y(a,b){b&&q(a,t(b));var c=a.onload;a.onload=function(d){c&&c(d);google.ps=google.ps.filter(function(e){return a!==e})};google.ps.push(a);document.body.appendChild(a)}google.as=y;function x(a){google.timers&&google.timers.load&&google.tick&&google.tick(\"load\",\"xjsls\");var b=r(\"SCRIPT\");b.onerror=function(){google.ple=1};b.onload=function(){google.ple=0};google.xjsus=void 0;y(b,a);google.aple=-1;google.dp=!0}\n",
      "function z(){var a=[u];if(!google.dp){for(var b=0;b<a.length;b++){var c=r(\"LINK\"),d=c,e=t(a[b]);if(e instanceof l)d.href=m(e).toString(),d.rel=\"preload\";else{if(p.indexOf(\"preload\")===-1)throw Error(\"a`preload\");e=n.test(e)?e:void 0;e!==void 0&&(d.href=e,d.rel=\"preload\")}c.setAttribute(\"as\",\"script\");document.body.appendChild(c)}google.dp=!0}};function A(a){var b=a.getAttribute(\"jscontroller\");return(b===\"UBXHI\"||b===\"R3fhkb\"||b===\"TSZEqd\")&&a.hasAttribute(\"data-src\")}function B(){for(var a=document.getElementsByTagName(\"img\"),b=0,c=a.length;b<c;b++){var d=a[b];if(d.hasAttribute(\"data-lzy_\")&&Number(d.getAttribute(\"data-atf\"))&1&&!A(d))return!0}return!1}for(var C=document.getElementsByTagName(\"img\"),D=0,E=C.length;D<E;++D){var F=C[D];Number(F.getAttribute(\"data-atf\"))&1&&A(F)&&(F.src=F.getAttribute(\"data-src\"))};var G,H,I,J,K;function L(){google.xjsu=u;f._F_jsUrl=u;J=function(){w()};G=!1;H=(st===1||st===3)&&!!google.caft&&!B();I=(st===2||st===3)&&!!google.rairicb&&!B();K=pod}function M(){G||H||I||(J(),G=!0)}setTimeout(function(){google&&google.tick&&google.timers&&google.timers.load&&google.tick(\"load\",\"xjspls\");L();if(H||I){if(H){var a=function(){H=!1;M()};google.caft(a);window.setTimeout(a,amd)}I&&(a=function(){I=!1;M()},(0,google.rairicb)(a),window.setTimeout(a,mmd));K&&(G||z())}else J()},0);})();window._ = window._ || {};window._DumpException = _._DumpException = function(e){throw e;};window._s = window._s || {};_s._DumpException = _._DumpException;window._qs = window._qs || {};_qs._DumpException = _._DumpException;(function(){var t=[1,64,0,0,0,0,4341760,0,1131520,135141401,1310720,8224,805324800,3,134217728,8448,269092904,1042313216,541065358,2224,188];window._F_toggles = window._xjs_toggles = t;})();window._F_installCss = window._F_installCss || function(css){};(function(){google.jl={bfl:0,dw:false,ine:false,ubm:false,uwp:true,vs:false};})();(function(){var pmc='{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:false,\\x22cgen\\x22:false,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22Clear Search\\x22,\\x22dym\\x22:\\x22Did you mean:\\x22,\\x22lcky\\x22:\\x22I\\\\u0026#39;m Feeling Lucky\\x22,\\x22lml\\x22:\\x22Learn more\\x22,\\x22psrc\\x22:\\x22This search was removed from your \\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003EWeb History\\\\u003C/a\\\\u003E\\x22,\\x22psrl\\x22:\\x22Remove\\x22,\\x22sbit\\x22:\\x22Search by image\\x22,\\x22srch\\x22:\\x22Google Search\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22rfs\\x22:[],\\x22stok\\x22:\\x220_VFDU5AaQUDxkqOrZFniAYF0T0\\x22}}';google.pmc=JSON.parse(pmc);})();(function(){var b=function(a){var c=0;return function(){return c<a.length?{done:!1,value:a[c++]}:{done:!0}}};\n",
      "var e=this||self;var g,h;a:{for(var k=[\"CLOSURE_FLAGS\"],l=e,n=0;n<k.length;n++)if(l=l[k[n]],l==null){h=null;break a}h=l}var p=h&&h[610401301];g=p!=null?p:!1;var q,r=e.navigator;q=r?r.userAgentData||null:null;function t(a){return g?q?q.brands.some(function(c){return(c=c.brand)&&c.indexOf(a)!=-1}):!1:!1}function u(a){var c;a:{if(c=e.navigator)if(c=c.userAgent)break a;c=\"\"}return c.indexOf(a)!=-1};function v(){return g?!!q&&q.brands.length>0:!1}function w(){return u(\"Safari\")&&!(x()||(v()?0:u(\"Coast\"))||(v()?0:u(\"Opera\"))||(v()?0:u(\"Edge\"))||(v()?t(\"Microsoft Edge\"):u(\"Edg/\"))||(v()?t(\"Opera\"):u(\"OPR\"))||u(\"Firefox\")||u(\"FxiOS\")||u(\"Silk\")||u(\"Android\"))}function x(){return v()?t(\"Chromium\"):(u(\"Chrome\")||u(\"CriOS\"))&&!(v()?0:u(\"Edge\"))||u(\"Silk\")}function y(){return u(\"Android\")&&!(x()||u(\"Firefox\")||u(\"FxiOS\")||(v()?0:u(\"Opera\"))||u(\"Silk\"))};var z=v()?!1:u(\"Trident\")||u(\"MSIE\");y();x();w();var A=!z&&!w(),D=function(a){if(/-[a-z]/.test(\"ved\"))return null;if(A&&a.dataset){if(y()&&!(\"ved\"in a.dataset))return null;a=a.dataset.ved;return a===void 0?null:a}return a.getAttribute(\"data-\"+\"ved\".replace(/([A-Z])/g,\"-$1\").toLowerCase())};var E=[],F=null;function G(a){a=a.target;var c=performance.now(),f=[],H=f.concat,d=E;if(!(d instanceof Array)){var m=typeof Symbol!=\"undefined\"&&Symbol.iterator&&d[Symbol.iterator];if(m)d=m.call(d);else if(typeof d.length==\"number\")d={next:b(d)};else throw Error(\"b`\"+String(d));for(var B=[];!(m=d.next()).done;)B.push(m.value);d=B}E=H.call(f,d,[c]);if(a&&a instanceof HTMLElement)if(a===F){if(c=E.length>=4)c=(E[E.length-1]-E[E.length-4])/1E3<5;if(c){c=google.getEI(a);a.hasAttribute(\"data-ved\")?f=a?D(a)||\"\":\"\":f=(f=\n",
      "a.closest(\"[data-ved]\"))?D(f)||\"\":\"\";f=f||\"\";if(a.hasAttribute(\"jsname\"))a=a.getAttribute(\"jsname\");else{var C;a=(C=a.closest(\"[jsname]\"))==null?void 0:C.getAttribute(\"jsname\")}google.log(\"rcm\",\"&ei=\"+c+\"&tgtved=\"+f+\"&jsname=\"+(a||\"\"))}}else F=a,E=[c]}window.document.addEventListener(\"DOMContentLoaded\",function(){document.body.addEventListener(\"click\",G)});}).call(this);\n",
      "  </script>\n",
      " </body>\n",
      "</html>\n",
      "\n"
     ]
    }
   ],
   "source": [
    "web=re.get(\"https://www.google.com/\")\n",
    "soup=BeautifulSoup(web.content, 'html.parser')\n",
    "print(soup.prettify())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0dbdb856-8e9f-423c-a08a-a1d50bf1b822",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<title>Google</title>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.title\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ebcb6b78-02bb-4ec6-b0f9-f430b3a634dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "title\n"
     ]
    }
   ],
   "source": [
    "print(soup.title.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "657e26e8-741d-4e66-8762-ec776d709ff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup.h1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e8725450-1925-4a59-86e6-16d751e543c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<a class=\"gb1\" href=\"https://www.google.com/imghp?hl=en&amp;tab=wi\">Images</a>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "17e21267-edc4-4852-8c14-bb514b25d601",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<p style=\"font-size:8pt;color:#70757a\">© 2024 - <a href=\"/intl/en/policies/privacy/\">Privacy</a> - <a href=\"/intl/en/policies/terms/\">Terms</a></p>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f4b2ffa-c1d0-4fb1-9b35-181c7a04b261",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
