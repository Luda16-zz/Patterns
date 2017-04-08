function AdapteeShipping(){
	this.request = function(origen, destino, peso){
		this.origin 	= origen;
		this.destino 	= destino;
		this.peso 		= peso;
		this.total 		= Math.round(Math.random()*12345)
		return this.total
	}
}


function TargetShipping(){
	this.login = function(credentials){

	};
	this.setOrigen(origen){
		//this.origen = origen;
	};
	this.setDestino(destino){
		//this.destino = destino;
	};
	this.calculate(peso){
		//this.peso  = peso;
		this.total = Math.round(Math.random()*4321);
	};
}

function ShippingAdapter(credentials){
	var targetShipping = new TargetShipping();
	targetShipping.login();

	return{
		request: function(origen, destino, peso){
			targetShipping.setOrigen(origen);
			targetShipping.setDestino(destino);
			return targetShipping.calculate(peso);
		}
	}
}

function Client(){
	this.run = function(){
		var oldInterface = new AdapteeShipping();
		var cost = oldInterface.request("1234", "321", 123.45);
		print(cost);

		var mycreds = "user/pass";
		var adapter = new ShippingAdapter(mycreds);
		var newCost = adapter.request("1234", "321", 123.45);

		print(newCost);
	}
}