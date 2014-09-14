import DS from 'ember-data';

export default DS.Model.extend({
    pickup_type: DS.attr('number'),
    departure_time_second: DS.attr('number'),
    arrival_time_minute: DS.attr('number'),
    stop_headsign: DS.attr('string'),
    shape_dist_traveled: DS.attr('number'),
    departure_time_minute: DS.attr('number'),
    arrival_time_second: DS.attr('number'),
    departure_time_hour: DS.attr('number'),
    stop_id: DS.attr('string'),
    drop_off_type: DS.attr('number'),
    arrival_time_hour: DS.attr('number'),
    trip_id: DS.attr('string'),
    departure_time: DS.attr('string'),
    arrival_time: DS.attr('string'),
    stop_sequence: DS.attr('number'),
    trip: DS.attr()
    //trip: DS.belongsTo('trip', {embedded: 'always'})
});
