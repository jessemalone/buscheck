"""empty message

Revision ID: 42cd873a6bd4
Revises: None
Create Date: 2014-08-24 14:30:08.623711

"""

# revision identifiers, used by Alembic.
revision = '42cd873a6bd4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar_dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.String(length=64), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('exception_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_calendar_dates_date'), 'calendar_dates', ['date'], unique=False)
    op.create_index(op.f('ix_calendar_dates_service_id'), 'calendar_dates', ['service_id'], unique=False)
    op.create_table('shapes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shape_id', sa.String(length=64), nullable=True),
    sa.Column('shape_pt_lat', sa.Float(), nullable=True),
    sa.Column('shape_pt_lon', sa.Float(), nullable=True),
    sa.Column('shape_pt_sequence', sa.Integer(), nullable=True),
    sa.Column('shape_dist_traveled', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shapes_shape_id'), 'shapes', ['shape_id'], unique=False)
    op.create_table('agencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agency_phone', sa.String(length=64), nullable=True),
    sa.Column('agency_fare_url', sa.String(length=255), nullable=True),
    sa.Column('agency_url', sa.String(length=255), nullable=True),
    sa.Column('agency_id', sa.String(length=64), nullable=True),
    sa.Column('agency_name', sa.String(length=128), nullable=True),
    sa.Column('agency_timezone', sa.String(length=64), nullable=True),
    sa.Column('agency_lang', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agencies_agency_id'), 'agencies', ['agency_id'], unique=False)
    op.create_table('trips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.String(length=64), nullable=True),
    sa.Column('route_id', sa.String(length=64), nullable=True),
    sa.Column('direction_id', sa.Integer(), nullable=True),
    sa.Column('trip_headsign', sa.String(length=128), nullable=True),
    sa.Column('shape_id', sa.String(length=64), nullable=True),
    sa.Column('service_id', sa.String(length=64), nullable=True),
    sa.Column('trip_id', sa.String(length=64), nullable=True),
    sa.Column('trip_short_name', sa.String(length=128), nullable=True),
    sa.Column('wheelchair_boarding', sa.Boolean(), nullable=True),
    sa.Column('bikes_allowed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trips_block_id'), 'trips', ['block_id'], unique=False)
    op.create_index(op.f('ix_trips_route_id'), 'trips', ['route_id'], unique=False)
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route_long_name', sa.String(length=128), nullable=True),
    sa.Column('route_type', sa.Integer(), nullable=True),
    sa.Column('route_text_color', sa.String(length=6), nullable=True),
    sa.Column('route_color', sa.String(length=6), nullable=True),
    sa.Column('agency_id', sa.String(length=64), nullable=True),
    sa.Column('route_id', sa.String(length=64), nullable=True),
    sa.Column('route_url', sa.String(length=255), nullable=True),
    sa.Column('route_desc', sa.String(length=255), nullable=True),
    sa.Column('route_short_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_routes_agency_id'), 'routes', ['agency_id'], unique=False)
    op.create_index(op.f('ix_routes_route_id'), 'routes', ['route_id'], unique=False)
    op.create_index(op.f('ix_routes_route_short_name'), 'routes', ['route_short_name'], unique=False)
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.String(length=64), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('monday', sa.Boolean(), nullable=True),
    sa.Column('tuesday', sa.Boolean(), nullable=True),
    sa.Column('wednesday', sa.Boolean(), nullable=True),
    sa.Column('thursday', sa.Boolean(), nullable=True),
    sa.Column('friday', sa.Boolean(), nullable=True),
    sa.Column('saturday', sa.Boolean(), nullable=True),
    sa.Column('sunday', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_calendar_end_date'), 'calendar', ['end_date'], unique=False)
    op.create_index(op.f('ix_calendar_service_id'), 'calendar', ['service_id'], unique=False)
    op.create_index(op.f('ix_calendar_start_date'), 'calendar', ['start_date'], unique=False)
    op.create_table('stops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stop_lat', sa.Float(), nullable=True),
    sa.Column('wheelchair_boarding', sa.Boolean(), nullable=True),
    sa.Column('stop_code', sa.Integer(), nullable=True),
    sa.Column('stop_lon', sa.Float(), nullable=True),
    sa.Column('stop_id', sa.String(length=64), nullable=True),
    sa.Column('stop_url', sa.String(length=255), nullable=True),
    sa.Column('parent_station', sa.String(length=128), nullable=True),
    sa.Column('stop_desc', sa.String(length=255), nullable=True),
    sa.Column('stop_name', sa.String(length=128), nullable=True),
    sa.Column('location_type', sa.Integer(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stops_stop_id'), 'stops', ['stop_id'], unique=False)
    op.create_index(op.f('ix_stops_stop_lat'), 'stops', ['stop_lat'], unique=False)
    op.create_index(op.f('ix_stops_stop_lon'), 'stops', ['stop_lon'], unique=False)
    op.create_table('stop_times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.String(length=64), nullable=True),
    sa.Column('arrival_time', sa.String(length=8), nullable=True),
    sa.Column('departure_time', sa.String(length=8), nullable=True),
    sa.Column('stop_id', sa.String(length=64), nullable=True),
    sa.Column('stop_sequence', sa.Integer(), nullable=True),
    sa.Column('stop_headsign', sa.String(length=128), nullable=True),
    sa.Column('pickup_type', sa.Integer(), nullable=True),
    sa.Column('drop_off_type', sa.Integer(), nullable=True),
    sa.Column('shape_dist_traveled', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stop_times_stop_id'), 'stop_times', ['stop_id'], unique=False)
    op.create_index(op.f('ix_stop_times_trip_id'), 'stop_times', ['trip_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stop_times_trip_id'), table_name='stop_times')
    op.drop_index(op.f('ix_stop_times_stop_id'), table_name='stop_times')
    op.drop_table('stop_times')
    op.drop_index(op.f('ix_stops_stop_lon'), table_name='stops')
    op.drop_index(op.f('ix_stops_stop_lat'), table_name='stops')
    op.drop_index(op.f('ix_stops_stop_id'), table_name='stops')
    op.drop_table('stops')
    op.drop_index(op.f('ix_calendar_start_date'), table_name='calendar')
    op.drop_index(op.f('ix_calendar_service_id'), table_name='calendar')
    op.drop_index(op.f('ix_calendar_end_date'), table_name='calendar')
    op.drop_table('calendar')
    op.drop_index(op.f('ix_routes_route_short_name'), table_name='routes')
    op.drop_index(op.f('ix_routes_route_id'), table_name='routes')
    op.drop_index(op.f('ix_routes_agency_id'), table_name='routes')
    op.drop_table('routes')
    op.drop_index(op.f('ix_trips_route_id'), table_name='trips')
    op.drop_index(op.f('ix_trips_block_id'), table_name='trips')
    op.drop_table('trips')
    op.drop_index(op.f('ix_agencies_agency_id'), table_name='agencies')
    op.drop_table('agencies')
    op.drop_index(op.f('ix_shapes_shape_id'), table_name='shapes')
    op.drop_table('shapes')
    op.drop_index(op.f('ix_calendar_dates_service_id'), table_name='calendar_dates')
    op.drop_index(op.f('ix_calendar_dates_date'), table_name='calendar_dates')
    op.drop_table('calendar_dates')
    ### end Alembic commands ###
