from qiskit import *

def teleportacion(qc, qr, crz, crx):
    # Par EPR. Puerta de Hadamard a qr[1] y luego Cnot.
    qc.h(qr[1])
    qc.cx(qr[1], qr[2])
    
    # Alice aplica Cnot (control qr[0]) y Hadamard a qr[0]
    qc.cx(qr[0], qr[1])
    qc.h(qr[0])
    
    # Medimos
    qc.measure(qr[0], crz)
    qc.measure(qr[1], crx)
        
    # Alice manda las mediciones a Bob y aplica
    # X si el segundo qubit es 1 (01)
    # Z si el primer qubit es 1 (10)
    # Y = XZ si ambos son 1 (11)
    qc.x(qr[2]).c_if(crx, 1)
    qc.z(qr[2]).c_if(crz, 1)

qr = QuantumRegister(3)
crx = ClassicalRegister(1)
crz = ClassicalRegister(1)
qc = QuantumCircuit(qr, crz, crx)

# Antes de llamar al algoritmo debemos poner el qubit
# qr[0] que queremos mandar al estado deseado. Lo
# dejamos en |0>.

teleportacion(qc, qr, crz, crx)