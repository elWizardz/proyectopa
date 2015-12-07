$(document).ready(function()
{	
	$('#editarProcesoButton').click(function(){
		var proceso = $('#procesosListEditar').val();
		if (proceso != null) {
			window.location.href = "/procesos/editar/" + proceso + "/";
		} else {
			window.location.href = "/procesos/";
		}
	});
	
	$('#borrarProcesoButton').click(function(){
		var proceso = $('#procesosListBorrar').val();
		if (proceso != null) {
			window.location.href = "/procesos/borrar/" + proceso + "/";
		} else {
			window.location.href = "/procesos/";
		}
	});
	
	$('#editarLineaButton').click(function(){
		var linea = $('#lineasListEditar').val();
		if (linea != null) {
			window.location.href = "/lineasdeproduccion/editar/" + linea + "/";
		} else {
			window.location.href = "/lineasdeproduccion/";
		}
	});
	
	$('#borrarLineaButton').click(function(){
		var linea = $('#lineasListBorrar').val();
		if (linea != null) {
			window.location.href = "/lineasdeproduccion/borrar/" + linea + "/";
		} else {
			window.location.href = "/lineasdeproduccion/";
		}
	});
	
	$('#verProductoButton').click(function(){
		var producto = $('#productosListVer').val();
		if (producto != null) {
			window.location.href = "/productos/ver/" + producto + "/";
		} else {
			window.location.href = "/productos/";
		}
	});
	
	$('#borrarProductoButton').click(function(){
		var producto = $('#productosListBorrar').val();
		if (producto != null) {
			window.location.href = "/productos/borrar/" + producto + "/";
		} else {
			window.location.href = "/productos/";
		}
	});
});

function checarValorProductoEditar(){
	
}