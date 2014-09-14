import Ember from 'ember';

export default Ember.Route.extend({
    model: function() { 
	var that = this;
	return new Ember.RSVP.Promise(function(resolve,reject) {
	    navigator.geolocation.getCurrentPosition(function(position) {
		var lat = position.coords.latitude;
		var long = position.coords.longitude;
		resolve(that.store.find('stop',{latitude:lat,longitude:long,distance:150}));
	    //return Ember..store.find('stop',{latitude:lat,longitude:long,distance:100});
	    })
	})
    }
 //   renderTemplate: function() {//
//	this.render({outlet: "home"})
//    },
   // afterModel: function(stops,transition) {
//	console.log(stops.get('firstObject').get('stopTimes'));
//	this.transitionTo("stops.stop" , stops.get('firstObject'));
 //   }
})
