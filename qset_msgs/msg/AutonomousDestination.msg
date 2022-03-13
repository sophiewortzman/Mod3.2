uint64 id
string name
# The geo point and heading will be used in LAT_LON coord type
geographic_msgs/GeoPoint globalPoint
float64 heading

# Otherwise the metrePoint will be used
geometry_msgs/PointStamped metrePoint
uint8 post_type
uint8 destination_type
uint8 coordinate_type

# this is the fiducial id if POST_TYPE_ARCUO_TAG
int32 tag_id
#this is the tag id for the other side of the gate for DESTINATION_TYPE_GATE
int32 tag_id_gate

float32 search_radius

uint8 POST_TYPE_GPS_POINT = 0
uint8 POST_TYPE_ARCUO_TAG = 1

uint8 DESTINATION_TYPE_POINT = 0
uint8 DESTINATION_TYPE_GATE = 1

uint8 COORDINATE_TYPE_LOCAL = 0
uint8 COORDINATE_TYPE_UTM = 1
uint8 COORDINATE_TYPE_LAT_LON = 2

