import Ember from 'ember';

var Router = Ember.Router.extend({
  location: FrontendENV.locationType
});

Router.map(function() {
  //this.route('stop', {path: '/stops/:stop_id'});

    this.route('stops', {path: 'stops'}, function() {
      this.route('stop', {path: '/:stop_id'});
    });
});

export default Router;
