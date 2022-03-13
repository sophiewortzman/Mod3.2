#include "pid.hpp"
#include "math.hpp"
#include <ros/ros.h>
namespace QSET::MATH
{
PID::PID(): PID(0.0f, 0.0f, 0.0f)
{
    //
}
PID::PID(const float kp, const float ki, const float kd, const float maxIntegrate): _kp(kp), _ki(ki), _kd(kd), _lastError(0.0f), _cumulativeError(0.0f), _maxIntegrate(maxIntegrate)
{

}

float
PID::GetValue(float error)
{
    _cumulativeError += error;

    if(std::fabs(_cumulativeError) > std::fabs(_maxIntegrate))
    {
        _cumulativeError = _maxIntegrate * getSign(_cumulativeError);
    }

    float derivativeError = error - _lastError;
    float ret = _kp * error + _ki * _cumulativeError + _kd * derivativeError;
    _lastError = error;
    return ret;
}

float
PID::GetValue(float error, float dt)
{
    if(dt <= 0.0f)
    {
        ROS_ERROR("Divide by 0 in PID %f", dt);
        return -1;
    }

    float dErr = (error - _lastError) / dt;
    _cumulativeError += (error * dt);

    if(std::fabs(_cumulativeError) > std::fabs(_maxIntegrate))
    {
        _cumulativeError = _maxIntegrate * getSign(_cumulativeError);
    }

    return _kp * error + _kd * dErr + _ki * _cumulativeError;
}

void
PID::SetGains(const float kp, const float ki, const float kd, const float maxIntegrate)
{
    _kd = kd;
    _ki = ki;
    _kp = kp;
    _maxIntegrate = maxIntegrate;
}

float
PID::getKp() const
{
    return _kp;
}

float
PID::getKi() const
{
    return _ki;
}

float
PID::getKd() const
{
    return _kd;
}
} // namespace QSET::MATH
