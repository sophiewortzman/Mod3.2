//
// Created by owen on 6/29/21.
//

#ifndef QSET_MATH_EKF_HPP
#define QSET_MATH_EKF_HPP

#include <Eigen/Core>
#include <Eigen/LU>

namespace QSET::MATH
{
/**
 * A Generic EKF class for use in localization
 * Based off of this paper:
 * https://www.cse.sc.edu/~terejanu/files/tutorialEKF.pdf
 */
class ExtendedKalmanFilter
{

public:
    /**
     * @brief Construct a new EKF
     * @param numStates the number states in the Kalman Filter
     */
    ExtendedKalmanFilter(const uint16_t numStates);

    /**
     * @brief Initializes the process noise and state vectors
     * @param xInit the initial state vector n x 1
     * @param pInit the initial covariance matrix n x n
     * @return if the initialization was successful
     */
    bool Initialize(const Eigen::MatrixXd &xInit, const Eigen::MatrixXd &pInit);

    /**
     * In the attached paper this is denoted as the derivation step
     * @param Fx n x 1 predicted state
     * @param F n x n Jacobian partial derivatives wrt x
     * @param Q n x n Process Noise Covariance
     */
    void Predict(const Eigen::MatrixXd &Fx, const Eigen::MatrixXd &F,
        const Eigen::MatrixXd &Q);

    /**
     * In the attached paper this is denoted as the Data assimilation step
     * @param z m x 1 observed state vector
     * @param R m x m observed covariance matrix
     * @param Hx m x 1 non-linear state observation matrix
     * @param H m x n state observation matrix
     */
    void Update(const Eigen::MatrixXd &z, const Eigen::MatrixXd &R,
        const Eigen::MatrixXd &Hx, const Eigen::MatrixXd &H);

    /**
     * In the attached paper this is denoted as the Data assimilation step
     * @param z m x 1 observed state vector
     * @param R m x m observed covariance matrix
     * @param H m x n state observation matrix
     */
    void Update(const Eigen::MatrixXd &z, const Eigen::MatrixXd &R,
        const Eigen::MatrixXd &H);

    /**
     *
     * @return n x 1 the current EKF state
     */
    inline const Eigen::MatrixXd
    GetState() const { return _X; };

    /**
     *
     * @return the curren EKF covariance
     */
    inline const Eigen::MatrixXd
    GetCovariance() const { return _P; };

    /// @brief indicates if the filter has been initialized with a starting state
    /// and covariance
    inline bool
    IsInitialized() const { return this->_isInitialized; }

private:
    /**
     * n x 1 state vector
     */
    Eigen::MatrixXd _X;

    /**
     * n x n covariance vector
     */
    Eigen::MatrixXd _P;

    /**
     * number of states in the state vector
     */
    uint16_t _numStates;

    /**
     * Indicates if the EKF has been initialized
     */
    bool _isInitialized;
};
} // namespace QSET::MATH
#endif // QSET_MATH_EKF_HPP
