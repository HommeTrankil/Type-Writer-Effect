# Type-Writer-Effect
inspired by @Traversy Media

{% load i18n staticfiles mezzanine_tags %}

<!-- separtor -->

<div class=" {% if p.slideAnim %} slideanim{% endif %}" style="background-color:#333333 !important">

		<div class="container">
		
<div class="text-center">
	
<p id="Para" style="color:white"></p> <!-- optional -->

<p style="background-color:#aaa">Hello <span id="Title"></span></p>

</div>

</div>
</div>

<script>

let speed = 5;
let pause = [{% for p in tw %}{{ p.pause }},{% endfor %}];
let list = [{% for p in tw %}'{{ p.text }}',{% endfor %}];
let listColor = [{% for p in tw %}'st{{ p.textStyle.id }}',{% endfor %}];

let counter = 0;

let str ="";
let strLength = 0;
let isBack= false;

var para="";//optional

function init(){
writeWord();
}

function writeWord(){

//when deleting letters
if (strLength <0){
  counter++;
  strLength=0;
  isBack = false;

  if ( counter > list.length-1 ){
    counter = 0;
    para = "";//optional
    document.getElementById("Para").innerHTML = para ; //optional

    }

  str="";
}

else if (strLength > (list[counter].length)-1 && !isBack){
	isBack = true;
    speed = pause[counter];

  para += str+"<br>" //optional
  document.getElementById("Para").innerHTML = para ;//optional
    }

else if (!isBack){
	prt(1);
	speed= Math.floor((Math.random() * 200) + 50);
    }

else if (isBack){
	prt(-1)
    speed = 20;
    }

document.getElementById("Title").className = listColor[counter]
document.getElementById("Title").innerHTML = str+'|' ;
setTimeout(writeWord, speed)
}

function prt(n){
str="";
strLength +=n;
for (let i=0;i <strLength;i++)
	str += list[counter][i]

}

</script>


<!-- //testimonial -->
