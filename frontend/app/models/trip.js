import DS from 'ember-data';

export default DS.Model.extend({
    wheelchair_boarding: DS.attr('boolean'),
    block_id: DS.attr('string'),
    bikes_allowed: DS.attr('boolean'),
    direction_id: DS.attr('number'),
    route_id: DS.attr('string'),
    trip_headsign: DS.attr('string'),
    service_id: DS.attr('string'),
    trip_id: DS.attr('string'),
    trip_short_name: DS.attr('string')
    
    
});
