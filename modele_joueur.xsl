<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"/>
<xsl:template match="/">
<html>
<head>
<style type ="text/css">
h1{color:green;}
h2{color:green;text-align:center;}
h3{text-indent:20px;color:blue;}
.defense{ border :1px black double;}
p{text-indent:40px;}
</style>
</head>
<body>
<h1 style="color:red; font-size:300%; text-align:center">Eventail :
<xsl:value-of select="joueur/@Nom"/>
</h1>
<h1>UTG</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='1']"/>
</p>
<div class="defense">
<h2>UTG : Défense contre 3B de MP</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='2']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='3']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='4']"/></p>
</div>
<div class="defense">
<h2>UTG : Défense contre 3B de CO</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='5']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='6']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='7']"/></p>

</div>
<div class="defense">
<h2>UTG : Défense contre 3B de BU</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='8']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='9']"/></p>


<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='10']"/></p>

</div>

<div class="defense">
<h2>UTG : Défense contre 3B de SB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='11']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='12']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='13']"/></p>

</div>

<div class="defense">
<h2>UTG : Défense contre 3B de BB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='14']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='15']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='16']"/></p>

</div>

<h1>MP</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='17']"/>
</p>
<div class="defense">
<h2>MP : Défense contre OR de UTG</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='18']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='19']"/></p>
<h3>3B en Value: (5Betl sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='20']"/></p>
</div>
<div class="defense">
<h2>MP : Défense contre 3B de CO</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='21']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='22']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='23']"/></p>

</div>
<div class="defense">
<h2>MP : Défense contre 3B de BU</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='24']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='25']"/></p>


<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='26']"/></p>

</div>

<div class="defense">
<h2>MP : Défense contre 3B de SB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='27']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='28']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='29']"/></p>

</div>

<div class="defense">
<h2>MP : Défense contre 3B de BB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='30']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='31']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='32']"/></p>

</div>

<h1>CO</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='33']"/>
</p>
<div class="defense">
<h2>CO : Défense contre OR de UTG</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='34']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='35']"/></p>
<h3>3B en Value: (5Betl sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='36']"/></p>
</div>
<div class="defense">
<h2>CO : Défense contre OR de MP</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='37']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='38']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet ) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='39']"/></p>

</div>
<div class="defense">
<h2>CO : Défense contre 3B de BU</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='40']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='41']"/></p>


<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='42']"/></p>

</div>

<div class="defense">
<h2>CO : Défense contre 3B de SB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='43']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='44']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='45']"/></p>

</div>

<div class="defense">
<h2>CO : Défense contre 3B de BB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='46']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='47']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='48']"/></p>

</div>
<h1>BU</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='49']"/>
</p>
<div class="defense">
<h2>BU : Défense contre OR de UTG</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='50']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='51']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='52']"/></p>
</div>
<div class="defense">
<h2>BU : Défense contre OR de MP</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='53']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='54']"/></p>
<h3>3Bet en Value: (Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='55']"/></p>

</div>
<div class="defense">
<h2>BU : Défense contre OR de CO</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='56']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='57']"/></p>


<h3>3Bet en Value: (5Bet sur 4Bet ) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='58']"/></p>

</div>

<div class="defense">
<h2>BU : Défense contre 3B de SB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='59']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='60']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='61']"/></p>

</div>

<div class="defense">
<h2>BU : Défense contre 3B de BB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='62']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='63']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='64']"/></p>

</div>

<h1>SB</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='65']"/>
</p>
<div class="defense">
<h2>SB : Défense contre OR de UTG</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='66']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='67']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='68']"/></p>
</div>
<div class="defense">
<h2>SB : Défense contre OR de MP</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='69']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='70']"/></p>
<h3>3Bet en Value: (Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='71']"/></p>

</div>
<div class="defense">
<h2>SB : Défense contre OR de CO</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='72']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='73']"/></p>


<h3>3Bet en Value: (5Bet sur 4Bet ) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='74']"/></p>

</div>

<div class="defense">
<h2>SB : Défense contre OR de BU</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='75']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='76']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='77']"/></p>

</div>

<div class="defense">
<h2>SB : Défense contre 3B de BB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='78']"/></p>
<h3>4Bet Bluff: (Fold sur 5Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='79']"/></p>
<h3>4Bet en Value: (Call sur 5Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='80']"/></p>

</div>

<h1>BB</h1>
<h3>Open Raise :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='81']"/>
</p>
<div class="defense">
<h2>BB : Défense contre OR de UTG</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='82']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='83']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='84']"/></p>
</div>
<div class="defense">
<h2>BB : Défense contre OR de MP</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='85']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='86']"/></p>
<h3>3Bet en Value: (Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='87']"/></p>

</div>
<div class="defense">
<h2>BB : Défense contre OR de CO</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='88']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet)  </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='89']"/></p>


<h3>3Bet en Value: (5Bet sur 4Bet ) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='90']"/></p>

</div>

<div class="defense">
<h2>BB : Défense contre OR de BU</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='91']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='92']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='93']"/></p>

</div>

<div class="defense">
<h2>BB : Défense contre OR de SB</h2>

<h3>CALL:</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='94']"/></p>
<h3>3Bet Bluff: (Fold sur 4Bet) : </h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='95']"/></p>
<h3>3Bet en Value: (5Bet sur 4Bet) :</h3>
<p>
<xsl:value-of select="/joueur/eventail[@id='96']"/></p>

</div>

</body>
</html>
</xsl:template>
</xsl:stylesheet>