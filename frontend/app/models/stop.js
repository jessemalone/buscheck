import DS from 'ember-data';

export default DS.Model.extend({
    stop_lat: DS.attr('number'),
    wheelchair_boarding: DS.attr('boolean'),
    stop_code: DS.attr('number'),
    stop_lon: DS.attr('number'),
    parent_station: DS.attr('string'),
    stop_url: DS.attr('string'),
    stop_id: DS.attr('string'),
    stop_desc: DS.attr('string'),
    stop_name: DS.attr('string'),
    zone_id: DS.attr('string'),
    stopTimes: DS.hasMany("stopTime", {async: true})
});
