// 
// THIS SCRIPT IS CREATED BY CHRISTIAN BRON
// USE ONLY WITH PYTHON FLASK OR DJANGO
// asDFS09102429062sdsad094
// 
var ERR_EXCEPTIONS = false
function $(q){return document.querySelector(q)}
function $print(p){console.log(p)}
function $CLASS(class_name){return document.getElementsByClassName(class_name)}
function $ID(id_name){return document.getElementById(id_name)}
function $goto(url){window.location.replace(url);}
function $json(str){return JSON.parse(str)}

function $DATA(d){
	var data_form = new FormData();
	for (var key in d){data_form.append(key, d[key])}
	return data_form
}

function $show_view(ids,classn){
 	panel_views = c(classn)
 	for (var i = 0; i < panel_views.length; i++) {
 		if(ids!=panel_views[i].id){panel_views[i].style.display="none"}
 		else{panel_views[i].style.display="block"}
 	}
 }

function $send(params){
	if(params.action==undefined){params.action='/no_url'}
	if(params.data==undefined){params.data=$DATA({'_DATA':'NULL'})}
	if(params.func==undefined){params.func=function(res){$print(res)}}
	if(params.method==undefined){params.method='POST'}
	if(params.async==undefined){params.async=false}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){if (this.readyState == 4 && this.status == 200) {
		params.func(this.responseText)
	}};
	xhttp.open(params.method,params.action,params.async);
	xhttp.send(params.data);
}

function $ELEMENT(el,qs){
	elem = document.createElement(el); 
	return elem
}

function $randint(size){
	return Math.floor(Math.random() * size); 
}

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}