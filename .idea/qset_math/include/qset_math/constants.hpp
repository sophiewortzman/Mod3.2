//
// Created by owen on 9/6/21.
//

#ifndef QSET_MATH_CONSTANTS_HPP
#define QSET_MATH_CONSTANTS_HPP

#include "math.hpp"

namespace QSET::CONSTANTS
{

/**
 * @brief the length of the upper arm
 */
constexpr float UpperArmLength = 0.5;
/**
 * @brief the length of the forearm
 */
constexpr float ForearmLength = 0.4;
/**
 * @brief the length of the forearm lever
 */
constexpr float ForearmLeverLength = 0.2;
/**
 * @brief the angle between the forearm lever and the forearm
 */
constexpr float ForearmLeverAngle = QSET::MATH::angleToRadians(25); // 155
/**
 * @brief the length of the linear actuator base
 */
constexpr float LinearActuatorBaseLength = 0.4;
/**
 * @brief the length of the linear actuator piston
 */
constexpr float LinearActuatorPistonLength = 0.3;
/**
 * @brief the linear actuator travel distance
 */
constexpr float LinearActuatorTravelDistance = 0.2;
/**
 * @brief the distance from the shoulder joint to the linear actuator mount
 */
constexpr float LinearActuatorMountDistanceFromShoulder = 0.1;
/**
 * @brief the distance from the elbow joint to the linear actuator mount
 */
constexpr float LinearActuatorMountDistanceFromElbow = UpperArmLength - LinearActuatorMountDistanceFromShoulder;
/**
 * @brief the radius of the wheel
 */
constexpr float WheelRadius = 0.2;
/**
 * @brief the diameter of the wheel
 */
constexpr float WheelDiameter = WheelRadius * 2.0f;
/**
 * @brief the distance between wheels in metres
 */
constexpr float AxleLength = 1.0f;

}

#endif //QSET_MATH_CONSTANTS_HPP
