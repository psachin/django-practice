var myVar=setInterval(function(){clock()},1000);

function displayDate()
{
    document.getElementById("demo").innerHTML=Date();
    // document.write("id is")
}

function greet_user(name,job)
{
    alert("Hello " + name + ", the " + job);
}

function summ(var1,var2)
{
    return document.getElementById("summ").innerHTML=(var1+var2);
}

// create new element
var para=document.createElement("p");
// create new text node
var node=document.createTextNode("This is new");
// add newly created textnode to new element
para.appendChild(node);


// get element by ID
var element=document.getElementById("div1");
// append element para to element div1
element.appendChild(para);


// remove element p2
var parent=document.getElementById("div1")
var child=document.getElementById("p2")
parent.removeChild(child)


// --------------------
// create js-objects

// using direct instance
person=new Object();
person.firstname="John";
person.lastname="Doe"
person.age="50";
person.eyecolor="blue";

// accessing properties
// alert(person.eyecolor)
// alert(person['eyecolor'])


// ---
// using object constructor

function person2(firstname,lastname,age,fruit) {
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.fruit=fruit;
}

// create instance of object
var father = new person2("Martin","Rob","35","apple")

// alter values
x=person2.firstname="rany"
person2.firstname="peter"

// print
// alert(x.toUpperCase())
// alert(person2.firstname.toUpperCase())


// --------------------
// adding methods to objects
function car(name,model,color,speed,price) {
    this.name=name;
    this.model=model;
    this.color=color;
    this.speed=speed;
    this.price=price;

    this.ChangePrice=ChangePrice;

    function ChangePrice(price) {
	this.price=price;
    }
}

var audi=new car("audi","c800","blue","800","10")
// alert(audi.price)

audi.ChangePrice("90")
// alert(audi.price)

// --------------------

href=document.write(location.href + "<br>");
pathname=document.write(location.pathname);
parent.appendChild(href)
parent.appendChild(pathname)

// --------------------

// redirects to w3school
function newDoc()
{
    window.location.assign("http://www.w3schools.com")
}


// --------------------


function clock()
{
    var d = new Date();
    var t = d.toLocaleTimeString();
    document.getElementById("clock").innerHTML=t;
}

