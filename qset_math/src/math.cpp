#include "math.hpp"
#include "sensor_msgs/Imu.h"
#include "tf2/LinearMath/Matrix3x3.h"
#include <Eigen/Eigen>
#include <Eigen/src/Core/Matrix.h>
#include "geometry_msgs/Point.h"
#include <cmath>
#include <geometry_msgs/Quaternion.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2/convert.h>
#include <tf2/transform_datatypes.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

namespace QSET::MATH
{

geographic_msgs::GeoPoint
fixToGeoPoint(const sensor_msgs::NavSatFix &a)
{
    geographic_msgs::GeoPoint temp;
    temp.latitude = a.latitude;
    temp.longitude = a.longitude;
    temp.altitude = a.altitude;
    return temp;
}

double
getGpsDistance(const geographic_msgs::GeoPoint &a, const geographic_msgs::GeoPoint &b)
{
    double lat1 = angleToRadians(a.latitude);
    double lat2 = angleToRadians(b.latitude);
    double temp = pow2(std::sin(angleToRadians(b.latitude - a.latitude) / 2)) +
        cos(lat1) * cos(lat2) * pow2(angleToRadians(b.longitude - a.longitude) / 2);
    return 2.0 * std::atan2(std::sqrt(temp), std::sqrt(temp - 1.0)) * EARTH_RADIUS;

}

void
setYaw(geometry_msgs::PoseWithCovarianceStamped &in, const double o)
{
    tf2::Quaternion q;
    q.setRPY(0, 0, o);
    q.normalize();
    geometry_msgs::Quaternion geo_q;
    tf2::convert<tf2::Quaternion, geometry_msgs::Quaternion>(q, geo_q);
    in.pose.pose.orientation = geo_q;
}

void
setYaw(geometry_msgs::PoseStamped &in, const double o)
{
    tf2::Quaternion q;
    q.setRPY(0, 0, o);
    q.normalize();
    geometry_msgs::Quaternion geo_q;
    tf2::convert<tf2::Quaternion, geometry_msgs::Quaternion>(q, geo_q);
    in.pose.orientation = geo_q;
}

void
setYaw(geometry_msgs::TransformStamped &transformStamped, const double o)
{
    tf2::Quaternion q;
    q.setRPY(0, 0, o);
    transformStamped.transform.rotation.x = q.x();
    transformStamped.transform.rotation.y = q.y();
    transformStamped.transform.rotation.z = q.z();
    transformStamped.transform.rotation.w = q.w();
}

double
getYaw(const tf2::Quaternion &q)
{
    tf2::Matrix3x3 m(q);
    double r, p, y;
    m.getRPY(r, p, y);
    return y;
}

std::tuple<double, double, double>
getRPY(const tf2::Quaternion &q)
{
    tf2::Matrix3x3 m(q);
    double r, p, y;
    m.getRPY(r, p, y);
    return {r, p, y};
}

sensor_msgs::Imu
removeGravityAccel(const sensor_msgs::Imu &msg)
{
    sensor_msgs::Imu ret = msg;
    const auto& q  = msg.orientation;
    Eigen::Vector3d w(0.0, 0.0, GravityAcceleration);

    Eigen::Vector4d Pp (q.w * w.x() + q.y * w.z() - q.z * w.y(),
        q.w * w.y() + q.z * w.x() - q.x * w.z(),
        q.w * w.z() + q.x * w.y() - q.y * w.x(),
        -q.x * w.x() - q.y * w.y() - q.z * w.z());

    ret.linear_acceleration.x -= Pp(0);
    ret.linear_acceleration.y -= Pp(1);
    ret.linear_acceleration.z -= Pp(2);

    return ret;
}
}
