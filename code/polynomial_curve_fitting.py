# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:53:38 2020

@author: Nirmal
"""

import numpy as np
import math as math
import matplotlib.pyplot as plt 

def compute_error(b, m, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        temp=y - (m * x + b)
        if temp < 0:
            temp = 0-temp
        temp = math.log(temp,10000)
        totalError += np.log(np.cosh((temp)))
        variance += (np.log(np.cosh((temp)))*np.log(np.cosh((temp))))

    totalError /= float(len(points)) 
    variance /= float(len(points))      
    #print("Degree = 1, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error2(b, m, c, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (c * x * x + m * x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (c * x * x + m * x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (c * x * x + m * x + b)),10000)))))
     
    totalError /= float(len(points)) 
    variance /= float(len(points))    
    #print("Degree = 2, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error3(b, m, c, d, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (d*x*x*x + c*x*x + m*x + b)),10000)))))
    
    totalError /= float(len(points)) 
    variance /= float(len(points)) 
    #print("Degree = 3, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error4(b, m, c, d, e, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000)))))
    
    totalError /= float(len(points)) 
    variance /= float(len(points))   
    #print("Degree = 4, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error5(b, m, c, d, e, f, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000)))))
    
    totalError /= float(len(points)) 
    variance /= float(len(points))    
    #print("Degree = 5, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error6(b, m, c, d, e, f, g, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000)))))
        
    totalError /= float(len(points)) 
    variance /= float(len(points))     
    #print("Degree = 6, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error7(b, m, c, d, e, f, g, h, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000)))))
        
    totalError /= float(len(points)) 
    variance /= float(len(points))    
    #print("Degree = 7, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance

def compute_error8(b, m, c, d, e, f, g, h, i, points):
    totalError = 0
    variance = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += np.log(np.cosh((math.log(np.abs(y - (i*x*x*x*x*x*x*x*x + h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))
        variance += (np.log(np.cosh((math.log(np.abs(y - (i*x*x*x*x*x*x*x*x + h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000))))*np.log(np.cosh((math.log(np.abs(y - (i*x*x*x*x*x*x*x*x + h*x*x*x*x*x*x*x + g*x*x*x*x*x*x + f*x*x*x*x*x + e*x*x*x*x + d*x*x*x + c*x*x + m*x + b)),10000)))))
        
    totalError /= float(len(points)) 
    variance /= float(len(points))    
    #print("Degree = 7, Variance = {0}, totalError = {1} \n".format(variance / float(len(points)), totalError))
    return totalError, variance    



def step_gradient(b_current,m_current,points,rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - ((m_current * x) + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - ((m_current * x) + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    return [new_b, new_m]

def step_gradient2(b_current,m_current,c_current,points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    return [new_b, new_m, new_c] 

def step_gradient3(b_current,m_current,c_current, d_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (d_current*x*x*x + c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    return [new_b, new_m, new_c, new_d]

def step_gradient4(b_current,m_current,c_current, d_current, e_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    e_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        e_gradient += -(1/N) * x * x * x * x * np.tanh(y - (e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    new_e = e_current - (rate * e_gradient)
    return [new_b, new_m, new_c, new_d, new_e] 

def step_gradient5(b_current,m_current,c_current, d_current, e_current, f_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    e_gradient = 0
    f_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        e_gradient += -(1/N) * x * x * x * x * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        f_gradient += -(1/N) * x * x * x * x * x * np.tanh(y - (f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    new_e = e_current - (rate * e_gradient)
    new_f = f_current - (rate * f_gradient)
    return [new_b, new_m, new_c, new_d, new_e, new_f]  

def step_gradient6(b_current,m_current,c_current, d_current, e_current, f_current, g_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    e_gradient = 0
    f_gradient = 0
    g_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        e_gradient += -(1/N) * x * x * x * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        f_gradient += -(1/N) * x * x * x * x * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        g_gradient += -(1/N) * x * x * x * x * x * x * np.tanh(y - (g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current)) 
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    new_e = e_current - (rate * e_gradient)
    new_f = f_current - (rate * f_gradient)
    new_g = g_current - (rate * g_gradient)
    return [new_b, new_m, new_c, new_d, new_e, new_f, new_g]

def step_gradient7(b_current,m_current,c_current, d_current, e_current, f_current, g_current, h_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    e_gradient = 0
    f_gradient = 0
    g_gradient = 0
    h_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        e_gradient += -(1/N) * x * x * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        f_gradient += -(1/N) * x * x * x * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        g_gradient += -(1/N) * x * x * x * x * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        h_gradient += -(1/N) * x * x * x * x * x * x * x * np.tanh(y - (h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    new_e = e_current - (rate * e_gradient)
    new_f = f_current - (rate * f_gradient)
    new_g = g_current - (rate * g_gradient)
    new_h = h_current - (rate * h_gradient)
    return [new_b, new_m, new_c, new_d, new_e, new_f, new_g, new_h]

def step_gradient8(b_current,m_current,c_current, d_current, e_current, f_current, g_current, h_current, i_current, points,rate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    d_gradient = 0
    e_gradient = 0
    f_gradient = 0
    g_gradient = 0
    h_gradient = 0
    i_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(1/N) * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        m_gradient += -(1/N) * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        c_gradient += -(1/N) * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        d_gradient += -(1/N) * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        e_gradient += -(1/N) * x * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        f_gradient += -(1/N) * x * x * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        g_gradient += -(1/N) * x * x * x * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        h_gradient += -(1/N) * x * x * x * x * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
        i_gradient += -(1/N) * x * x * x * x * x * x * x * x * np.tanh(y - (i_current*x*x*x*x*x*x*x*x + h_current*x*x*x*x*x*x*x + g_current*x*x*x*x*x*x + f_current*x*x*x*x*x + e_current*x*x*x*x + d_current*x*x*x + c_current*x*x + m_current*x + b_current))
    new_b = b_current - (rate * b_gradient)
    new_m = m_current - (rate * m_gradient)
    new_c = c_current - (rate * c_gradient)
    new_d = d_current - (rate * d_gradient)
    new_e = e_current - (rate * e_gradient)
    new_f = f_current - (rate * f_gradient)
    new_g = g_current - (rate * g_gradient)
    new_h = h_current - (rate * h_gradient)
    new_i = i_current - (rate * i_gradient)
    return [new_b, new_m, new_c, new_d, new_e, new_f, new_g, new_h, new_i]    

def gradient_descent_runner(points,rate,num_iterations,M):
    m=10
    b=10
    c=10
    d=10
    e=10
    f=10
    g=10
    h=10
    if M == 1:
        for i in range(num_iterations):
            b,m = step_gradient(b,m, np.array(points),rate)
        return [b,m]
  
    elif M == 2:
        for i in range(num_iterations):
            b,m,c = step_gradient2(b,m,c, np.array(points),rate)
        return [b,m,c] 
    elif M == 3:
        for i in range(num_iterations):
            b,m,c,d = step_gradient3(b,m,c, d, np.array(points),rate)
        return [b,m,c,d]
    
    elif M == 4:
        for i in range(num_iterations):
            b,m,c,d,e = step_gradient4(b,m,c, d, e, np.array(points),rate)
        return [b,m,c,d,e]
        
    elif M == 5:
        for i in range(num_iterations):
            b,m,c,d,e,f = step_gradient5(b,m,c, d, e, f, np.array(points),rate)
        return [b,m,c,d,e,f]
        
    elif M == 6:
        for i in range(num_iterations):
            b,m,c,d,e,f,g = step_gradient6(b,m,c, d, e, f, g, np.array(points),rate)
        return [b,m,c,d,e,f,g]

    elif M == 7:
        for i in range(num_iterations):
            b,m,c,d,e,f,g,h = step_gradient7(b,m,c, d, e, f, g, h, np.array(points),rate)
        return [b,m,c,d,e,f,g,h]

    elif M == 8:
        for i in range(num_iterations):
            b,m,c,d,e,f,g,h,i = step_gradient8(b,m,c, d, e, f, g, h,i, np.array(points),rate)
        return [b,m,c,d,e,f,g,h,i]
    


def run():
    #for 20 points
    #points = np.loadtxt("mini_data07.txt",delimiter=",")
    #for 100 points
    points = np.loadtxt("data07.txt",delimiter=",")
    print(points)
    train_data_points = points[:80]
    test_data_points = points[80:]
    print("\n\nTaring data ...")
    print(train_data_points)
    print("\n\nTesting data ...")
    print(test_data_points)
    print("\n\n\n")
    x = points[:, 0]
    y = points[:, 1]
    plt.plot(x, y, 'o')
    rate = 0.01
    M=1
    min=1000000
    degree=1
    num_iterations = 1000
    trainError_list = []
    testError_list = []
    for i in range(8):
        
        if M == 1:
            [b,m] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([m,b], test_data_points[:,0]), 'r-')
            trainError1, trainVariance1 = compute_error(b, m, train_data_points)
            testError1, testVariance1 = compute_error(b, m, test_data_points)
            print("Degree = 1,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance1, trainError1, testVariance1, testError1))
            trainError_list.append(trainError1)
            testError_list.append(testError1)
            if min > testError1:
               min = testError1
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error(b, m, train_data_points)))
        elif M == 2:
            [b,m,c] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([c,m,b], test_data_points[:,0]), 'r-')
            trainError2, trainVariance2 = compute_error2(b, m, c, train_data_points)
            testError2, testVariance2 = compute_error2(b, m, c, test_data_points)
            print("Degree = 2,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance2, trainError2, testVariance2, testError2))
            trainError_list.append(trainError2)
            testError_list.append(testError2)
            if min > testError2:
               min = testError2
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, error = {4}".format(num_iterations, b, m, c, compute_error2(b, m, c, train_data_points)))
        elif M == 3:
            [b,m,c,d] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([d,c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([d,c,m,b], test_data_points[:,0]), 'r-')
            trainError3, trainVariance3 = compute_error3(b, m, c, d, train_data_points)
            testError3, testVariance3 = compute_error3(b, m, c, d, test_data_points)
            print("Degree = 3,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance3, trainError3, testVariance3, testError3))
            trainError_list.append(trainError3)
            testError_list.append(testError3)
            if min > testError3:
               min = testError3
               degree = M
           # print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, error = {5}".format(num_iterations, b, m, c, d, compute_error3(b, m, c, d, train_data_points)))
        elif M == 4:
            [b,m,c,d,e] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([e,d,c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([e,d,c,m,b], test_data_points[:,0]), 'r-')
            trainError4, trainVariance4 = compute_error4(b, m, c, d, e, train_data_points)
            testError4, testVariance4 = compute_error4(b, m, c, d, e, test_data_points)
            print("Degree = 4,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance4, trainError4, testVariance4, testError4))
            trainError_list.append(trainError4)
            testError_list.append(testError4)
            if min > testError4:
               min = testError4
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, error = {6}".format(num_iterations, b, m, c, d, e, compute_error4(b, m, c, d, e, train_data_points)))
        elif M == 5:
            [b,m,c,d,e,f] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([f,e,d,c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([f,e,d,c,m,b], test_data_points[:,0]), 'r-')
            trainError5, trainVariance5 = compute_error5(b, m, c, d, e, f, train_data_points)
            testError5, testVariance5 = compute_error5(b, m, c, d, e, f, test_data_points)
            print("Degree = 5,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance5, trainError5, testVariance5, testError5))
            trainError_list.append(trainError5)
            testError_list.append(testError5)
            if min > testError5:
               min = testError5
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, error = {7}".format(num_iterations, b, m, c, d, e, f, compute_error5(b, m, c, d, e, f, train_data_points)))
        elif M == 6:
            [b,m,c,d,e,f,g] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([g,f,e,d,c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([g,f,e,d,c,m,b], test_data_points[:,0]), 'r-')
            trainError6, trainVariance6 = compute_error6(b, m, c, d, e, f, g, train_data_points)
            testError6, testVariance6 = compute_error6(b, m, c, d, e, f, g, test_data_points)
            print("Degree = 6,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance6, trainError6, testVariance6, testError6))
            trainError_list.append(trainError6)
            testError_list.append(testError6)
            if min > testError6:
               min = testError6
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, error = {8}".format(num_iterations, b, m, c, d, e, f, g, compute_error6(b, m, c, d, e, f, g, train_data_points)))
        elif M == 7:
            [b,m,c,d,e,f,g,h] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            plt.plot(train_data_points[:,0],np.polyval([h,g,f,e,d,c,m,b], train_data_points[:,0]), 'b-')
            plt.plot(test_data_points[:,0],np.polyval([h,g,f,e,d,c,m,b], test_data_points[:,0]), 'r-')
            trainError7, trainVariance7 = compute_error7(b, m, c, d, e, f, g, h, train_data_points)
            testError7, testVariance7 = compute_error7(b, m, c, d, e, f, g, h, test_data_points)
            print("Degree = 7,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance7, trainError7, testVariance7, testError7))
            trainError_list.append(trainError7)
            testError_list.append(testError7)
            if min > testError7:
               min = testError7
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, h = {8}, error = {9}".format(num_iterations, b, m, c, d, e, f, g, h, compute_error7(b, m, c, d, e, f, g, h, train_data_points)))
        
        elif M == 8:
            [b,m,c,d,e,f,g,h,i] = gradient_descent_runner(train_data_points,rate,num_iterations,M)
            #plt.plot(train_data_points[:,0],np.polyval([i,h,g,f,e,d,c,m,b], train_data_points[:,0]), 'b-')
            #plt.plot(test_data_points[:,0],np.polyval([i,h,g,f,e,d,c,m,b], test_data_points[:,0]), 'r-')
            trainError8, trainVariance8 = compute_error8(b, m, c, d, e, f, g, h, i, train_data_points)
            testError8, testVariance8 = compute_error8(b, m, c, d, e, f, g, h, i, test_data_points)
            print("Degree = 8,  tainVariance = {0},  trainError = {1},  testVariance = {2},  testError = {3} \n".format(trainVariance8, trainError8, testVariance8, testError8))
            trainError_list.append(trainError8)
            testError_list.append(testError8)
            if min > testError8:
               min = testError8
               degree = M
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, h = {8}, error = {9}".format(num_iterations, b, m, c, d, e, f, g, h, compute_error7(b, m, c, d, e, f, g, h, train_data_points)))

        M = M + 1
    print("Best suited Degree of polynomial = {0}, error = {1}".format(degree, min))
    M = degree
    if M == 1:
        [b,m] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}".format(b, m))
    elif M == 2:
        [b,m,c] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}".format(b, m, c))
    elif M == 3:
        [b,m,c,d] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}".format(b, m, c, d))
           # print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, error = {5}".format(num_iterations, b, m, c, d, compute_error3(b, m, c, d, train_data_points)))
    elif M == 4:
        [b,m,c,d,e] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}, e = {4}".format(b, m, c, d, e))
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, error = {6}".format(num_iterations, b, m, c, d, e, compute_error4(b, m, c, d, e, train_data_points)))
    elif M == 5:
        [b,m,c,d,e,f] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}, e = {4}, f = {5}".format(b, m, c, d, e, f))
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, error = {7}".format(num_iterations, b, m, c, d, e, f, compute_error5(b, m, c, d, e, f, train_data_points)))
    elif M == 6:
        [b,m,c,d,e,f,g] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}, e = {4}, f = {5}, g = {6}".format(b, m, c, d, e, f, g))    
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, error = {8}".format(num_iterations, b, m, c, d, e, f, g, compute_error6(b, m, c, d, e, f, g, train_data_points)))
    elif M == 7:
        [b,m,c,d,e,f,g,h] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}, e = {4}, f = {5}, g = {6}, h = {7}".format(b, m, c, d, e, f, g, h))    
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, h = {8}, error = {9}".format(num_iterations, b, m, c, d, e, f, g, h, compute_error7(b, m, c, d, e, f, g, h, train_data_points)))
    elif M == 8:
        [b,m,c,d,e,f,g,h,i] = gradient_descent_runner(points,rate,num_iterations,M)
        print("Co-efficeints: b = {0}, m = {1}, c = {2}, d = {3}, e = {4}, f = {5}, g = {6}, h = {7}, i = {8} ".format(b, m, c, d, e, f, g, h, i))    
            #print("After {0} iterations b = {1}, m = {2}, c = {3}, d = {4}, e = {5}, f = {6}, g = {7}, h = {8}, error = {9}".format(num_iterations, b, m, c, d, e, f, g, h, compute_error7(b, m, c, d, e, f, g, h, train_data_points))) 

    plt.show() 
    plt.plot([1,2,3,4,5,6,7,8], trainError_list, 'b--')
    plt.plot([1,2,3,4,5,6,7,8], testError_list, 'r--')       
    plt.show()    
if __name__ == '__main__':
    run()