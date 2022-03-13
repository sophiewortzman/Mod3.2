//
// Created by owen on 6/29/21.
//

#include "ekf.hpp"

using namespace QSET::MATH;

inline bool
checkDims (const Eigen::MatrixXd &m, const uint16_t numRows, const uint16_t numCols)
{
    return ((numRows > 0) && (numCols > 0) && m.rows() == numRows && m.cols() == numCols);
}


ExtendedKalmanFilter::ExtendedKalmanFilter(const uint16_t numStates) : _numStates(numStates), _isInitialized(false)
{
    _X = Eigen::MatrixXd::Zero(_numStates, 1);
    _P = Eigen::MatrixXd::Zero(_numStates, _numStates);
}

bool
ExtendedKalmanFilter::Initialize(const Eigen::MatrixXd &xInit, const Eigen::MatrixXd &pInit )
{
    const bool rightDims = checkDims(xInit, _numStates, 1) && checkDims(pInit, _numStates, _numStates);

//    if(rightDims)
    {
        _X = xInit;
        _P = pInit;
        this->_isInitialized = true;
    }

    return rightDims;
}

void
ExtendedKalmanFilter::Predict(const Eigen::MatrixXd &Fx, const Eigen::MatrixXd &F, const Eigen::MatrixXd &Q)
{
    if(!this->_isInitialized) { return; }

    this->_X = Fx;

    this->_P = F * this->_P * F.transpose();

    this->_P = this->_P + Q;
}

void
ExtendedKalmanFilter::Update(const Eigen::MatrixXd &z, const Eigen::MatrixXd &R, const Eigen::MatrixXd &H)
{
    if(!this->_isInitialized) { return; }

    const auto pHT = _P * H.transpose();
    const auto S = H * pHT  + R;
    const auto K = pHT * S.inverse();
    const auto I = Eigen::MatrixXd::Identity(_numStates, _numStates);
    _X = _X + K * (z - H * _X);
    _P = (I - K * H) * _P;
}

void
ExtendedKalmanFilter::Update(const Eigen::MatrixXd &z, const Eigen::MatrixXd &R, const Eigen::MatrixXd &Hx, const Eigen::MatrixXd &H)
{
    if(!this->_isInitialized) { return; }

    const auto pHT = _P * H.transpose();
    const auto S = H * pHT + R;
    const auto K = pHT * S.inverse();
    const auto I = Eigen::MatrixXd::Identity(_numStates, _numStates);

    _X = _X * K * (z - Hx);
    _P = (I - K * H) * _P;
}

