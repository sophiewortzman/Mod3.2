//
// Created by owen on 9/5/21.
//

#ifndef SIMULATION_LINEARELBOWPLUGIN_HPP
#define SIMULATION_LINEARELBOWPLUGIN_HPP

#include "math.hpp"

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ros/ros.h>
#include <std_msgs/Float64.h>
#include <functional>

namespace QSET::SIMULATION
{

/**
 * @brief A gazebo plugin to control the elbow with a linear actuator
 */
class LinearElbowPlugin : public gazebo::ModelPlugin
{
public:
    /**
     * @brief initializes the class
     */
    LinearElbowPlugin();

    /**
     * @brief this is run when the rover is loaded into gazebo
     */
    void Load(gazebo::physics::ModelPtr _model, sdf::ElementPtr _sdf) override;

    /**
     * @brief this updates the state of the arm
     * This is run by gazebo every physics iteration
     */
    void Update() const;
private:

    /**
     * @brief a callback for the linear actuator desied velocity
     * @param msg the velocity value
     */
    void linearActuatorVelocityCallback(const std_msgs::Float64 &msg);

private:
    /**
     * @brief pointer to the linear actuator joint, used to set velocity/force
     */
    gazebo::physics::JointPtr linearActuatorJoint;

    /**
     * @brief pointer to the joint between the upper arm and the linear actuator
     * Used to set the position of the joint
     */
    gazebo::physics::JointPtr upperArmLinearActuatorJoint;

    /**
     * @brief pointer to the joint between the forearm lever and the linear actuator
     * Used to set the position of the joint
     */
    gazebo::physics::JointPtr linearActuatorLeverJoint;

    /**
     * @brief pointer to the physics update event connection
     */
    gazebo::event::ConnectionPtr updateConnection;

    /**
     * @brief pointer to an instance of a NodeHandle
     * used to create subscribers
     */
    std::unique_ptr<ros::NodeHandle> nh;

    /**
     * @brief a subscriber for the incoming linear actuator force topic
     */
    ros::Subscriber linAccForceSub;

    /**
     * @brief the requested force on the linear actuator
     */
    double linearActuatorForce;
};


}

GZ_REGISTER_MODEL_PLUGIN(QSET::SIMULATION::LinearElbowPlugin)

#endif //SIMULATION_LINEARELBOWPLUGIN_HPP
