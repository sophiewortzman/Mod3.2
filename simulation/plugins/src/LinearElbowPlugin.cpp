//
// Created by owen on 9/5/21.
//

#include "LinearElbowPlugin.hpp"

#include "math.hpp"
#include "constants.hpp"
#include "ros/init.h"

#include <istream>
using namespace QSET::SIMULATION;
using namespace QSET::MATH;
using namespace QSET;
using namespace gazebo;

void
LinearElbowPlugin::Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
{
    this->linearActuatorJoint = _model->GetJoint("linear_actuator");
    this->upperArmLinearActuatorJoint = _model->GetJoint("upper_arm_linear_actuator_base");
    this->linearActuatorLeverJoint = _model->GetJoint("linear_actuator_forearm_lever");

    if (!ros::isInitialized())
    {
        int argc = 0;
        char ** argv = nullptr;
        ros::init(argc, argv, "linear_actuator");
    }

    nh.reset(new ros::NodeHandle("linear_actuator"));
    this->linAccForceSub = nh->subscribe("/linear_actuator_force", 1, &LinearElbowPlugin::linearActuatorVelocityCallback, this);
    this->updateConnection = event::Events::ConnectWorldUpdateBegin(std::bind(&LinearElbowPlugin::Update, this));
}

void
LinearElbowPlugin::Update() const
{
    ros::spinOnce();
    const double linearActuatorLength = CONSTANTS::LinearActuatorBaseLength + CONSTANTS::LinearActuatorPistonLength + this->linearActuatorJoint->Position();
    const double upperAngleNonTransformed = getAngleFromThreeSides(CONSTANTS::LinearActuatorMountDistanceFromElbow, linearActuatorLength, CONSTANTS::ForearmLeverLength);
    const double leverAngleNonTransformed = getAngleFromThreeSides(CONSTANTS::ForearmLeverLength, linearActuatorLength, CONSTANTS::LinearActuatorMountDistanceFromElbow);

    const double linearActuatorUpperArmAngle = QSET::MATH::PI - ((upperAngleNonTransformed > 0.0 && !std::isnan(upperAngleNonTransformed)) ? upperAngleNonTransformed : 0.01);
    const double linearActuatorLeverAngle = QSET::MATH::PI -  ((leverAngleNonTransformed > 0.0 && !std::isnan(leverAngleNonTransformed)) ? leverAngleNonTransformed : 0.01);

    if(upperAngleNonTransformed <= 0.0 || leverAngleNonTransformed <= 0.0 || std::isnan(upperAngleNonTransformed) || std::isnan(leverAngleNonTransformed) )
    {
        ROS_ERROR("BAD ANGLE");
        this->linearActuatorJoint->SetForce(0, -0.1);
    }
    else
    {
        ROS_INFO("USING FORCE %f", this->linearActuatorForce);
        this->linearActuatorJoint->SetForce(0, this->linearActuatorForce);
    }

    this->upperArmLinearActuatorJoint->SetPosition(0, linearActuatorUpperArmAngle);
    this->linearActuatorLeverJoint->SetPosition(0, linearActuatorLeverAngle);
}

void
LinearElbowPlugin::linearActuatorVelocityCallback(const std_msgs::Float64 &msg)
{
    this->linearActuatorForce = msg.data;
}

LinearElbowPlugin::LinearElbowPlugin() : linearActuatorForce(0.0) {}
