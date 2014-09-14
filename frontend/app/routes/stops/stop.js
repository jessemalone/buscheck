import Ember from 'ember';

export default Ember.Route.extend({
    model: function(params) {
	console.log(params);
	return this.store.find('stop', params.stop_id);
    }
//    renderTemplate: function() {
//	this.render({outlet: "stop"});
//    }
});
