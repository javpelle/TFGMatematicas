from qiskit import *

def codificacionSuperdensa(qc, qr, bits):
    if bits < 0 or bits > 3:
        return "El valor de bits debe ser 0, 1, 2 o 3."
    
    # Par EPR. Puerta de Hadamard al primer qubit y luego Cnot.
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    
    # Alice aplica puerta a su qubit conforme al valor de bits
    if bits == 0:
        pass
    elif bits == 1:
        qc.x(qr[0])
    elif bits == 2:
        qc.y(qr[0])
    else: # bits == 3
        qc.z(qr[0])
        
    # Alice transmite el qubit a Bob que aplica Cnot y luego Hadamard al qubit recibido
    qc.cx(qr[0], qr[1])
    qc.h(qr[0])
    
    # Medimos
    qc.measure_all()
    
qr = QuantumRegister(2)
qc = QuantumCircuit(qr)
value = 2
codificacionSuperdensa(qc, qr, value)