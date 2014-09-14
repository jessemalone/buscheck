import Ember from 'ember';

export default Ember.Controller.extend({

    setupController: function(controller, stop) {
	console.log(controllers.stops);
	controller.set('model',stop);
    }
});
