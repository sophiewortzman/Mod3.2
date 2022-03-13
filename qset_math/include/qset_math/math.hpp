#ifndef QSET_MATH_HPP_
#define QSET_MATH_HPP_

#include <geographic_msgs/GeoPoint.h>
#include <sensor_msgs/NavSatFix.h>
#include <geometry_msgs/TransformStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <geometry_msgs/Quaternion.h>
#include <tf2/LinearMath/Quaternion.h>
#include "geometry_msgs/PointStamped.h"
#include "geometry_msgs/Pose.h"
#include "geometry_msgs/PoseStamped.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/Vector3.h"
#include "sensor_msgs/Imu.h"
#include "types.hpp"

namespace QSET::MATH
{
/**
 * @brief a constant for the radius of the earth
 *
 */
constexpr double EARTH_RADIUS = 6378100.0;
constexpr double PI = 3.141592653;
constexpr double HalfPI = PI / 2.0;
constexpr double ThreePIOnTwo = PI * 1.5;
constexpr double TwoPI = PI * 2;
constexpr double GravityAcceleration = 9.80665; // m/s^2

/**
 * @brief converts NavSatFi to GeoPoint msgs
 * This function does not preserve the GPS status data conveyed in the fix msg
 * @param fix input msg
 * @return geopoint msg with fix data
 */
geographic_msgs::GeoPoint fixToGeoPoint(const sensor_msgs::NavSatFix &fix);

/**
 * @brief gets distance in m between 2 gps points
 * @param a the first point
 * @param b the second point
 * @return the distance in m between provided points
 */
double getGpsDistance(const geographic_msgs::GeoPoint &a, const geographic_msgs::GeoPoint &b);

/**
 * @brief gets distance in m between 2 gps points
 * @param point the first point
 * @param fix the second point
 * @return the distance in m between provided points
 */
inline double
getGpsDistance(const geographic_msgs::GeoPoint &point, const sensor_msgs::NavSatFix &fix) {return getGpsDistance(point, fixToGeoPoint(fix));};

/**
 * @brief Converts angles in degrees to radians
 */
inline constexpr double
angleToRadians(const double degrees) {return degrees * PI / 180.0;};

/**
 * @brief squares a number
 */
template<typename T>
inline constexpr T
pow2(const T x)
{
    return std::pow(x, 2);
}

/**
 * @brief converts angle in radians to degrees
 */
template<typename T>
inline constexpr T
radiansToDegrees(const T x)
{
    return x * 180.0 / PI;
}

/**
 * @brief checks if the difference between 2 numbers is less than an epsilon
 * @tparam T the type of number
 * @param lhs one of the numbers
 * @param rhs the other number
 * @param epsilon the maximum distance to be considered equal
 * @return true if difference is less than epsilon, false otherwise
 */
template<typename T>
inline constexpr bool
isEqual(const T& lhs, const T& rhs, const double epsilon = 0.0001)
{
    return std::fabs(lhs - rhs) < epsilon;
}

/**
 * @brief gets the magnitude of a given vector
 * @return magnitude of vector
 */
template <typename T>
inline constexpr T
getMagnitude(const T& a, const T& b, const T& c = 0)
{
    return std::sqrt(pow2(a) + pow2(b) + pow2(c));
}

/**
 * @brief gets the magnitude of a point
 */
inline float
getMagnitude(const Point2D &point)
{
    return getMagnitude(point.x, point.y);
}

/// @brief gets the sign of a number
template <typename T>
inline T
getSign(T val)
{
    return (T(0) < val) - (val < T(0));
}

/**
 * @brief gets an angle between 0 and 2pi
 */
inline float
getNormalizedAngleRads(const float rads)
{
    return std::fmod(rads, TwoPI);
}

/**
 * @brief adds yaw data to a pose message
 * @param in reference to the Pose msg to have yaw added to
 * @param o the yaw to be set
 */
void setYaw(geometry_msgs::PoseWithCovarianceStamped &in, const double o);

/**
 * @brief adds yaw data to a pose msg
 */
void setYaw(geometry_msgs::PoseStamped &in, const double o);

/**
 * @brief adds yaw data to a transform msg
 */
void setYaw(geometry_msgs::TransformStamped &transformStamped, const double o);

/**
 * @brief converts quaternion types
 * @param q input
 * @return converted quaternion
 */
inline tf2::Quaternion
convertQuaternion(const geometry_msgs::Quaternion &q)
{
    return {q.x, q.y, q.z, q.w};
}

/**
 * @brief gets the yaw from a quaternion
 * @param q the quaternion to get yaw from
 * @return yaw
 */
double getYaw(const tf2::Quaternion &q);

/**
 * @brief overload of getYaw
 */
inline double
getYaw(const geometry_msgs::Quaternion &q)
{
    return getYaw(convertQuaternion(q));
};

/**
 * @brief gets the angle C
 * @return then angle of the side across from length c
 */
inline constexpr double
getAngleFromThreeSides(const double a, const double b, const double c)
{
    return std::acos((pow2(a) + pow2(b) - pow2(c)) / (2 * a * b) );
}

template<typename T>
inline T
getWithinBounds(const T in, const T upper, const T lower)
{
    return std::max(lower, std::min(in, upper));
}

std::tuple<double, double, double>
getRPY(const tf2::Quaternion &q);

inline std::tuple<double, double, double>
getRPY(const geometry_msgs::Quaternion &q)
{
    return getRPY(convertQuaternion(q));
}

sensor_msgs::Imu
removeGravityAccel(const sensor_msgs::Imu &msg);

inline geometry_msgs::Point
getPointFromVector(const geometry_msgs::Vector3 &vec)
{
    geometry_msgs::Point point;
    point.x = vec.x;
    point.y = vec.y;
    point.z = vec.z;
    return point;
}

inline geometry_msgs::Point
getTransformedPoint(const geometry_msgs::Point &point, const geometry_msgs::Transform &transform)
{
    auto pointCopy = point;
    pointCopy.x += transform.translation.x;
    pointCopy.y += transform.translation.y;
    pointCopy.z += transform.translation.z;
    return pointCopy;
}

inline geometry_msgs::PointStamped
getTransformedPoint(const geometry_msgs::PointStamped &point, const geometry_msgs::Transform &transform)
{
    auto pointCopy = point;
    pointCopy.point = getTransformedPoint(point.point, transform);
    return pointCopy;
}

inline geometry_msgs::PointStamped
getTransformedPoint(const geometry_msgs::PointStamped &point, const geometry_msgs::TransformStamped &transform)
{
    ROS_WARN_STREAM_COND(point.header.frame_id != transform.header.frame_id, "Transforming between " << point.header.frame_id << " and " << transform.header.frame_id << " these should be the same");
    auto pointCopy = point;
    pointCopy.point = getTransformedPoint(point.point, transform.transform);
    return pointCopy;
}

inline geometry_msgs::PointStamped
getPointFromPose(const geometry_msgs::PoseStamped &pose)
{
    geometry_msgs::PointStamped ret;
    ret.header = pose.header;
    ret.point = pose.pose.position;
    return ret;
}

inline
geometry_msgs::PoseStamped
getPoseFromPoint(const geometry_msgs::PointStamped &pose)
{
    geometry_msgs::PoseStamped ret;
    ret.header = pose.header;
    ret.pose.position = pose.point;
    return ret;
}


} // namespace QSET::MATH

#endif // QSET_MATH_HPP_
