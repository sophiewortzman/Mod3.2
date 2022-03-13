
#ifndef QSET_MATH_PID_HPP_
#define QSET_MATH_PID_HPP_

#include <limits>
namespace QSET::MATH
{
/**
 * @brief a basic pid class
 */
class PID
{
public:

    /// @brief creates an empty PID object
    PID();
    /// @brief creats a PID object with set values
    PID(const float kp, const float ki, const float kd, float maxIntegrate = std::numeric_limits<float>::infinity());

    /// @brief gets the control value based on the error
    float GetValue(float error);

    /// @brief gets the control value based on error and delta time
    float GetValue(float error, float dt);

    /// @brief sets the gains of the controller
    void SetGains(const float kp, const float ki, const float kd, float maxIntegrate = std::numeric_limits<float>::infinity());

    /// @brief gets the kp value
    float getKp() const;

    /// @brief gets the ki value
    float getKi() const;

    /// @brief  gets the kd value
    float getKd() const;

private:
    /// @brief the proportional term
    float _kp;
    /// @brief gets the integrated term
    float _ki;

    /// @brief the derivative term
    float _kd;
    /// @brief the last error recoreded
    float _lastError;

    /// @brief the total error recoreded
    float _cumulativeError;

    /// @brief the max value of the integrated term
    float _maxIntegrate;
};


} // namespace QSET::MATH
#endif //QSET_MATH_PID_HPP_
