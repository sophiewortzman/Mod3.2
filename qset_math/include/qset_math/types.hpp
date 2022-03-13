//
// Created by owen on 9/6/21.
//

#ifndef QSET_MATH_TYPES_HPP
#define QSET_MATH_TYPES_HPP

#include <ostream>
#include <ros/ros.h>
namespace QSET
{
/**
 * @brief a 2D point type
 */
struct Point2D
{
    /**
     * @brief creates a point with a given x and y value
     * @param x
     * @param y
     */
    Point2D(const float x, const float y): x(x), y(y) {};
    /**
     * @brief the default constructor
     */
    Point2D() : Point2D(0.0f, 0.0f) {};

    /// @brief the x value of the point
    float x;
    /// @brief the y value of the point
    float y;

    /**
     * @brief adds 2 points
     */
    inline Point2D
    friend
    operator+(const Point2D& lhs, const Point2D& rhs)
    {
        return Point2D(lhs.x + rhs.x, lhs.y + rhs.y);
    }

    /**
     * @brief subtracts 2 points
     */
    inline Point2D
    friend
    operator-(const Point2D& lhs, const Point2D &rhs)
    {
        return Point2D(lhs.x - rhs.x, lhs.y - rhs.y);
    }

    /**
     * @brief multiplies both of the parts of the point by some value
     */
    inline Point2D
    friend
    operator*(const Point2D& lhs, const float rhs)
    {
        return Point2D(lhs.x * rhs, lhs.y * rhs);
    }
    /**
     * @brief multiplies both of the parts of the point by some value
     */
    inline Point2D
    friend
    operator*(const float lhs, const Point2D& rhs)
    {
        return rhs * lhs;
    }
    /**
     * @brief divides both x and y by some value
     */
    inline Point2D
    friend
    operator/(const Point2D& lhs, float rhs)
    {
        return Point2D(lhs.x / rhs, lhs.y / rhs);
    }

    /**
     * @brief negates a point
     */
    inline Point2D
    friend
    operator-(const Point2D& rhs)
    {
        return Point2D(rhs.x * -1.0, rhs.y * -1.0);
    }

    /**
     * @brief handy print operator for a point
     */
    inline friend std::ostream &
    operator<< (std::ostream &out, const Point2D &p)
    {
        out << "{x: " << p.x << ", y: " << p.y << "}";
        return out;
    }

};

/**
 * @brief a type that handles data that can timeout
 * @tparam T the datatype that can be timed out
 */
template <class T>
class TimeoutData
{
public:
    /**
     * @brief set the initial value and timeout
     * @param v initial value for the data
     * @param to timeout value
     */
    TimeoutData(const T &v, double to) : value(v), recvTime(ros::Time::now()), timeout(to) {};

    /**
     * @brief set the timeout
     * @param to timeout value
     */
    TimeoutData(double to): value(), recvTime(0.0), timeout(to) {};

    /**
     * @brief default constructor, SetTimeout should be used if using this funciton
     */
    TimeoutData(): value(), recvTime(0.0), timeout(0.0) {};

    /**
     * @brief sets the timeout value
     * @param to number of seconds to timeout
     */
    void
    SetTimeout(const double to)
    {
        timeout = ros::Duration(to);
    }

    /**
     * @brief updates the data and resets the timeout
     * @param v new value for the data
     */
    void
    Update(const T &v)
    {
        value = v;
        recvTime = ros::Time::now();
    }

    /**
     * @brief checks if the data has timed out yet
     * @return true if the data is old, false otherwise
     */
    bool
    IsDataTimeout() const
    {
        return (ros::Time::now() - recvTime) > timeout;
    }

    /**
     * @brief gets the stored data
     * @return the stored data
     */
    T
    GetData() const
    {
        return value;
    }

private:
    /**
     * @brief the current data
     */
    T value;
    /**
     * @brief holds the time the data was recieved
     */
    ros::Time recvTime;
    /**
     * @brief the amount of time the data is considered "good" for
     */
    ros::Duration timeout;
};

}

#endif //QSET_MATH_TYPES_HPP
