from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
root=Tk()
root.title('Waveform viewer')
root.geometry("+400+100")
var1=StringVar()
var1.set("None")
var=StringVar()
var.set("None")
var2=StringVar()
var2.set("None")
frame1=LabelFrame(root,padx=10,pady=10,text='Choose the type of RL circuit')
frame2=LabelFrame(root,padx=10,pady=10,text='Choose the type of RC circuit')
frame3=LabelFrame(root,padx=10,pady=10,text='Choose the type of RLC circuit')
top=None
top1=None
def window(val):
    global top
    if top is not None:
        top.destroy()
    if val=='RC0':   #RC circuit without source
            top=Toplevel()
            top.title('RC circuit without source')
            top.geometry("+300+150")
            clicked=StringVar()
            clicked.set('None')
            #Label(top,text='Window for RC with no source').pack()
            def update_button(*args):
                 
                 if i_1.get() and i_2.get()  and i_4.get() and i_5.get() and i_6.get() and i_7.get():
                    button_t.config(state=NORMAL)
                    button.config(state=NORMAL)
                 elif i_1.get() and i_2.get()  and i_4.get():
                    button_t.config(state=NORMAL)
                    button.config(state=DISABLED)
            
                 else:
                    button.config(state=DISABLED)
                    button_t.config(state=DISABLED)
            i_1=StringVar()
            i_1.trace_add("write",update_button)
            i_2=StringVar()
            i_2.trace_add("write",update_button)
            #i_3=StringVar()
            #i_3.trace_add("write",update_button)
            i_4=StringVar()
            i_4.trace_add("write",update_button)
            i_5=StringVar()
            i_5.trace_add("write",update_button)
            i_6=StringVar()
            i_6.trace_add("write",update_button)
            i_7=StringVar()
            i_7.trace_add("write",update_button)
            my_lR=Label(top,text='Enter value of equivalent resistance(in ohms):')
            my_lR.grid(row=0,column=0)
            Entry(top,textvariable=i_1).grid(row=0,column=1,sticky=W+E) #i_1 value of Req
            my_lC=Label(top,text='Enter value of equivalent capacitance(in farads):')
            my_lC.grid(row=1,column=0)
            Entry(top,textvariable=i_2).grid(row=1,column=1,sticky=W+E) #i_2 value of Ceq
            #mylV=Label(top,text="Enter value of voltage source(in volts): ")
            #mylV.grid(row=2,column=0)
            #Entry(top,textvariable=i_3).grid(row=2,column=1,sticky=W+E)
            mylV0=Label(top,text="Enter value of initial voltage across equivalent capacitor(in volts): ")
            mylV0.grid(row=2,column=0)
            Entry(top,textvariable=i_4).grid(row=2,column=1,sticky=W+E) #i_4 initial condition of capacitor
            mylRu=Label(top,text="Choose a resistor from ciruit to view its waveforms: ")
            mylRu.grid(row=3,column=0)
            Entry(top,textvariable=i_5).grid(row=3,column=1,sticky=W+E) #i_5 value of resistance
            plt.close('all')
            frame5=LabelFrame(top,padx=10,pady=10)
            def showRC0(val):
                 val=clicked.get()
                 if val=="Amps":
                      global p 
                      p=val
                      frame5.grid_forget()
                      
                      frame5.grid(row=5,column=0)
                      Label(frame5,text='Initial value(in amps)').grid(row=0,column=0)
                      i_6.set("")
                      Entry(frame5,textvariable=i_6).grid(row=0,column=1)  #i_6 stores inital value
                      Label(frame5,text='Steady state value(in amps)').grid(row=1,column=0)
                      i_7.set("")
                      Entry(frame5,textvariable=i_7).grid(row=1,column=1) #i_7 stores steady state value
                      button.grid(row=6,column=0,pady=5)
                      button_t.grid(row=7,column=0,pady=5)
                 if val=="Volts":
                      p=val
                      frame5.grid_forget()
                      #plt.figure("Resistor Voltage with no source")
                      frame5.grid(row=5,column=0)
                      Label(frame5,text='Initial value(in volts)').grid(row=0,column=0)
                      i_6.set("")
                      Entry(frame5,textvariable=i_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in volts)').grid(row=1,column=0)
                      i_7.set("")
                      Entry(frame5,textvariable=i_7).grid(row=1,column=1)
                      button.grid(row=6,column=0,pady=5)
                      button_t.grid(row=7,column=0,pady=5)
            Label(top,text='Enter initial and steady state values across selected resistor in units of').grid(row=4,column=0)    
            drop=OptionMenu(top,clicked,"Amps","Volts",command=showRC0)
            drop.config(width=20)
            drop.grid(row=4,column=1)
            def time_constantRC0(val1,val2,val4):
                plt.close("Resistor Voltage with no source")
                plt.close("Resistor Current with no source")
                global t
                global tau
                tau=float(val1)*float(val2)
                if abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,500,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                #voltage across capacitor
                tau=float(val1)*float(val2) #val1 is Req,val2 is Ceq,val3 is V(0+)
                #print(tau)
                #Label(top,text='Time constant(in seconds)= '+str(tau)).grid(row=6,column=0)
                V_C=(float(val4)*np.exp(-t/tau))
                print(type(V_C))
                #current across capacitor
                I_C=(-float(val4)*np.exp(-t/tau))/float(val1)
                plt.figure("Capacitor voltage with no source")
                plt.plot(t,V_C,label='capacitor voltage',color='blue')
                plt.autoscale()
                plt.ylabel('Voltage(in volts)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveforms of capacitor voltage in transient analysis with no external source connected')
                plt.legend()
                plt.figure("Capacitor current with no source")
                plt.plot(t,I_C,label='capacitor current',color='red')
                plt.autoscale()
                plt.ylabel('Current(in amps)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveform of current through capacitor in transient analysis with no external source connected')
                plt.legend()
                plt.show()
            def resistanceRC0(val,v1,v2,v3,v4):
                plt.close("Capacitor voltage with no source")
                plt.close("Capacitor current with no source")
                global t
                global tau
                tau=float(v3)*float(v4)
                if abs(tau)<0.00001:
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,300,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                
                if val=="Volts":
                     plt.close('all')
                     initial=float(v1)
                     steady_state=float(v2)
                     
                     V_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor Voltage with no source")
                     plt.plot(t,V_R,label='resistor voltage',color='green')
                     plt.autoscale()
                     
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Voltage(in volts)')
                     plt.title('Waveforms of voltage across '+i_5.get()+' ohm resistor with no external source connected')
                     
                     plt.legend()
                     
                     plt.show()
                if val=="Amps":
                     plt.close('all')
                     initial=float(v1)
                     steady_state=float(v2)
                     I_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     #plt.figure('Resistor current with no source')
                     plt.figure("Resistor Current with no source")
                     plt.plot(t,I_R,label='resistor current',color='purple')
                     
                     plt.autoscale()
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Current(in amps)')
                     plt.title('Waveforms of current through '+i_5.get()+' ohm resistor with no external source connected')
                     plt.legend()
                     
                     plt.show()    
            button=Button(top,text='Click to view waveforms of the resistor selected',command=lambda:resistanceRC0(p,i_6.get(),i_7.get(),i_1.get(),i_2.get()),state=DISABLED)
            button.grid(row=5,column=0,columnspan=2,pady=5)
            button_t=Button(top,text='Click to view waveforms of equivalent capacitor',command=lambda:time_constantRC0(i_1.get(),i_2.get(),i_4.get()),state=DISABLED)
            button_t.grid(row=6,column=0,columnspan=2,pady=5)
    if val=='RC1': #RC circuit with source 
            top=Toplevel()
            top.title('RC circuit with source')
            clicked=StringVar()
            clicked.set('None')
            top.geometry("+300+150")
            #Label(top,text='Window for RC with source').pack()
            def update_button(*args):
                 
                 if input_1.get() and input_2.get() and input_3.get() and input_4.get() and input_5.get() and input_6.get() and input_7.get():
                    button_t.config(state=NORMAL)
                    button.config(state=NORMAL)
                 elif input_1.get() and input_2.get() and input_3.get() and input_4.get():
                    button_t.config(state=NORMAL)
                    button.config(state=DISABLED)
            
                 else:
                    button.config(state=DISABLED)
                    button_t.config(state=DISABLED)
            input_1=StringVar()
            input_1.trace_add("write",update_button)
            input_2=StringVar()
            input_2.trace_add("write",update_button)
            input_3=StringVar()
            input_3.trace_add("write",update_button)
            input_4=StringVar()
            input_4.trace_add("write",update_button)
            input_5=StringVar()
            input_5.trace_add("write",update_button)
            input_6=StringVar() #stores the initial value
            input_6.trace_add("write",update_button)
            input_7=StringVar()#stores the steady state value
            input_7.trace_add("write",update_button)
            input_8=StringVar() #stores the initial value
            input_8.trace_add("write",update_button)
            input_9=StringVar()#stores the steady state value
            input_9.trace_add("write",update_button)
            my_labelR=Label(top,text='Enter value of equivalent resistance(in ohms):')
            my_labelR.grid(row=0,column=0)
            Entry(top,textvariable=input_1).grid(row=0,column=1,sticky=W+E)
            my_labelC=Label(top,text='Enter value of equivalent capacitance(in farads):')
            my_labelC.grid(row=1,column=0)
            Entry(top,textvariable=input_2).grid(row=1,column=1,sticky=W+E)
            mylabelV=Label(top,text="Enter value of voltage source(in volts): ")
            mylabelV.grid(row=2,column=0)
            Entry(top,textvariable=input_3).grid(row=2,column=1,sticky=W+E)
            mylabelV0=Label(top,text="Enter value of initial voltage across equivalent capacitor(in volts): ")
            mylabelV0.grid(row=3,column=0)
            Entry(top,textvariable=input_4).grid(row=3,column=1,sticky=W+E)
            mylabelRu=Label(top,text="Choose a resistor from circuit to view its waveforms: ")
            mylabelRu.grid(row=4,column=0)
            Entry(top,textvariable=input_5).grid(row=4,column=1,sticky=W+E)
            plt.close('all')
            frame5=LabelFrame(top,padx=10,pady=10)
            def show(val): #in this window enter the value of inital conditions of resistor
                 val=clicked.get()
                 if val=="Amps":
                      global p 
                      p=val
                      frame5.grid_forget()
                      
                      frame5.grid(row=6,column=0)
                      Label(frame5,text='Initial value(in amps)').grid(row=0,column=0)
                      input_6.set("")
                      Entry(frame5,textvariable=input_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in amps)').grid(row=1,column=0)
                      input_7.set("")
                      Entry(frame5,textvariable=input_7).grid(row=1,column=1)
                      button.grid(row=7,column=0,pady=5)
                      button_t.grid(row=8,column=0,pady=5)
                 if val=="Volts":
                      p=val
                      frame5.grid_forget()
                      #plt.figure("Resistor Voltage")
                      frame5.grid(row=6,column=0)
                      Label(frame5,text='Initial value(in volts)').grid(row=0,column=0)
                      input_6.set("")
                      Entry(frame5,textvariable=input_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in volts)').grid(row=1,column=0)
                      input_7.set("")
                      Entry(frame5,textvariable=input_7).grid(row=1,column=1)
                      button.grid(row=7,column=0,pady=5)
                      button_t.grid(row=8,column=0,pady=5)
            Label(top,text='Enter initial and steady state values across selected resistor in units of').grid(row=5,column=0)
            drop=OptionMenu(top,clicked,"Amps","Volts",command=show)
            drop.config(width=20)
            drop.grid(row=5,column=1)
            def time_constant(val1,val2,val3,val4):
                plt.close("Resistor voltage with source")
                plt.close("Resistor current with source")
                global t
                global tau
                tau=float(val1)*float(val2)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,500,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                #voltage across capacitor
                
                #print(tau)
                #Label(top,text='Time constant(in seconds)= '+str(tau)).grid(row=6,column=0)
                V_C=float(val3)*(1-np.exp(-t/tau)) +(float(val4)*np.exp(-t/tau))
                print(type(V_C))
               
                #current across capacitor
                I_C=((float(val3)-float(val4))*np.exp(-t/tau))/float(val1)
                plt.figure("Capacitor voltage")
                plt.plot(t,V_C,label='capacitor voltage',color='blue')
                plt.ylabel('Voltage(in volts)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveforms of capacitor voltage in transient analysis with external source connected')
                plt.legend()
                plt.figure("Capacitor current")
                plt.plot(t,I_C,label='capacitor current',color='red')
                plt.ylabel('Current(in amps)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveform of current through capacitor in transient analysis with external source connected')
                plt.legend()
                plt.show()
            def resistance(val,val1,val2,val3,val4): #to plot voltage and current across resistor
                plt.close('Capacitor voltage')
                plt.close('Capacitor current')
                global t
                global tau
                #t=np.arange(0,10*3.14,0.01)
                tau=float(val3)*float(val4)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<=500:
                    t=np.linspace(0,500,500)
                if abs(tau)>500:
                    t=np.linspace(0,1000,500)
                if val=="Volts":
                     plt.close('all')
                     initial=float(val1)
                     steady_state=float(val2)
                     V_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor voltage with source")
                     plt.plot(t,V_R,label='resistor voltage',color='green')
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Voltage(in volts)')
                     plt.title('Waveforms of voltage across '+input_5.get()+' ohm resistor with external source connected')
                     plt.legend()
                     plt.show()
                if val=="Amps":
                     plt.close('all')
                     initial=float(val1)
                     steady_state=float(val2)
                     I_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor current with source")
                     plt.plot(t,I_R,label='resistor current',color='purple')
                     
                     plt.title('Waveforms of current through '+input_5.get()+' ohm resistor with external source connected')
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Current(in amps)')
                     plt.legend()
                     plt.show()
            button=Button(top,text='Waveforms of the resistor selected',command=lambda:resistance(p,input_6.get(),input_7.get(),input_1.get(),input_2.get()),state=DISABLED)
            button.grid(row=6,column=0,columnspan=2,pady=5)
            button_t=Button(top,text='Waveforms of equivalent capacitor',command=lambda:time_constant(input_1.get(),input_2.get(),input_3.get(),input_4.get()),state=DISABLED)
            button_t.grid(row=7,column=0,columnspan=2,pady=5)
    if val=="RL0":
            top=Toplevel()
            top.title('RL circuit without source')
            top.geometry("+300+150")
            clicked=StringVar()
            clicked.set('None')
            def update_button(*args):
                 
                 if i_1.get() and i_2.get()  and i_4.get() and i_5.get() and i_6.get() and i_7.get():
                    button_t.config(state=NORMAL)
                    button.config(state=NORMAL)
                 elif i_1.get() and i_2.get()  and i_4.get():
                    button_t.config(state=NORMAL)
                    button.config(state=DISABLED)
            
                 else:
                    button.config(state=DISABLED)
                    button_t.config(state=DISABLED)
            i_1=StringVar()
            i_1.trace_add("write",update_button)
            i_2=StringVar()
            i_2.trace_add("write",update_button)
            #i_3=StringVar()
            #i_3.trace_add("write",update_button)
            i_4=StringVar()
            i_4.trace_add("write",update_button)
            i_5=StringVar()
            i_5.trace_add("write",update_button)
            i_6=StringVar()
            i_6.trace_add("write",update_button)
            i_7=StringVar()
            i_7.trace_add("write",update_button)
            my_lR=Label(top,text='Enter value of equivalent resistance(in ohms):')
            my_lR.grid(row=0,column=0)
            Entry(top,textvariable=i_1).grid(row=0,column=1,sticky=W+E) #i_1 value of Req
            my_lC=Label(top,text='Enter value of equivalent inductance(in henry):')
            my_lC.grid(row=1,column=0)
            Entry(top,textvariable=i_2).grid(row=1,column=1,sticky=W+E) #i_2 value of Leq
            #mylV=Label(top,text="Enter value of voltage source(in volts): ")
            #mylV.grid(row=2,column=0)
            #Entry(top,textvariable=i_3).grid(row=2,column=1,sticky=W+E)
            mylV0=Label(top,text="Enter value of initial current through equivalent inductor(in amps): ")
            mylV0.grid(row=2,column=0)
            Entry(top,textvariable=i_4).grid(row=2,column=1,sticky=W+E) #i_4 initial condition of capacitor
            mylRu=Label(top,text="Choose a resistor from circuit to view its waveforms: ")
            mylRu.grid(row=3,column=0)
            Entry(top,textvariable=i_5).grid(row=3,column=1,sticky=W+E) #i_5 value of resistance
            plt.close('all')
            frame5=LabelFrame(top,padx=10,pady=10)
            def showRL0(val):
                 val=clicked.get()
                 if val=="Amps":
                      global p 
                      p=val
                      frame5.grid_forget()
                      #plt.figure("Resistor Current with no source")
                      frame5.grid(row=5,column=0)
                      Label(frame5,text='Initial value(in amps)').grid(row=0,column=0)
                      i_6.set("")
                      Entry(frame5,textvariable=i_6).grid(row=0,column=1)  #i_6 stores inital value
                      Label(frame5,text='Steady state value(in amps)').grid(row=1,column=0)
                      i_7.set("")
                      Entry(frame5,textvariable=i_7).grid(row=1,column=1) #i_7 stores steady state value
                      button.grid(row=6,column=0,pady=5)
                      button_t.grid(row=7,column=0,pady=5)
                 if val=="Volts":
                      p=val
                      frame5.grid_forget()
                      #plt.figure("Resistor Voltage with no source")
                      frame5.grid(row=5,column=0)
                      Label(frame5,text='Initial value(in volts)').grid(row=0,column=0)
                      i_6.set("")
                      Entry(frame5,textvariable=i_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in volts)').grid(row=1,column=0)
                      i_7.set("")
                      Entry(frame5,textvariable=i_7).grid(row=1,column=1)
                      button.grid(row=6,column=0,pady=5)
                      button_t.grid(row=7,column=0,pady=5)
            Label(top,text='Enter initial and steady state values across selected resistor in units of').grid(row=4,column=0)    
            drop=OptionMenu(top,clicked,"Amps","Volts",command=showRL0)
            drop.config(width=20)
            drop.grid(row=4,column=1)
            def time_constantRL0(val1,val2,val4): #val4 is initial condition
                plt.close("Resistor Voltage with no source")
                plt.close("Resistor Current with no source")
                global t
                global tau
                tau=float(val2)/float(val1)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<=500:
                    t=np.linspace(0,500,500)
                if abs(tau)>500:
                    t=np.linspace(0,1000,500)
                #voltage across capacitor
                tau=float(val2)/float(val1) #val1 is Req,val2 is Leq,val3 is V(0+)
                #print(tau)
                #Label(top,text='Time constant(in seconds)= '+str(tau)).grid(row=6,column=0)
                I_L=float(val4)*np.exp(-t/tau)
                #print(type(V_C))
                #current across capacitor
                V_L=((-float(val4))*float(val1))*np.exp(-t/tau)
                plt.figure("Inductor voltage with no source")
                plt.plot(t,V_L,label='inductor voltage',color='blue')
                plt.autoscale()
                plt.ylabel('Voltage(in volts)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveforms of inductor voltage in transient analysis with no external source connected')
                plt.legend()
                plt.figure("Inductor current with no source")
                plt.plot(t,I_L,label='Inductor current',color='red')
                plt.autoscale()
                plt.ylabel('Current(in amps)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveform of current through inductor in transient analysis with no external source connected')
                plt.legend()
                plt.show()
            def resistanceRL0(val,v1,v2,v3,v4):
                plt.close("Inductor voltage with no source")
                plt.close("Inductor current with no source")
                global t
                global tau
                tau=float(v4)/float(v3)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.001,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,500,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                if val=="Volts":
                     plt.close('all')
                     initial=float(v1)
                     steady_state=float(v2)
                     V_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor Voltage with no source")
                     plt.plot(t,V_R,label='resistor voltage',color='green')
                     plt.autoscale()
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Voltage(in volts)')
                     plt.title('Waveforms of voltage across '+i_5.get()+' ohm resistor with no external source connected')
                     plt.legend()
                     plt.show()
                if val=="Amps":
                     plt.close('all')
                     initial=float(v1)
                     steady_state=float(v2)
                     I_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     #plt.figure('Resistor current with no source')
                     plt.figure("Resistor Current with no source")
                     plt.plot(t,I_R,label='resistor current',color='purple')
                     plt.autoscale()
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Current(in amps)')
                     plt.title('Waveforms of current through '+i_5.get()+' ohm resistor with no external source connected')
                     plt.legend()
                     plt.show()    
            button=Button(top,text='Waveforms of the resistor selected',command=lambda:resistanceRL0(p,i_6.get(),i_7.get(),i_1.get(),i_2.get()),state=DISABLED)
            button.grid(row=5,column=0,columnspan=2,pady=5)
            button_t=Button(top,text='Waveforms of equivalent inductor',command=lambda:time_constantRL0(i_1.get(),i_2.get(),i_4.get()),state=DISABLED)
            button_t.grid(row=6,column=0,columnspan=2,pady=5)
    if val=="RL1":
            top=Toplevel()
            top.title('RL circuit with source')
            clicked=StringVar()
            clicked.set('None')
            top.geometry("+300+150")
            #Label(top,text='Window for RC with source').pack()
            def update_button(*args):
                 
                 if input_1.get() and input_2.get() and input_3.get() and input_4.get() and input_5.get() and input_6.get() and input_7.get():
                    button_t.config(state=NORMAL)
                    button.config(state=NORMAL)
                 elif input_1.get() and input_2.get() and input_3.get() and input_4.get():
                    button_t.config(state=NORMAL)
                    button.config(state=DISABLED)
            
                 else:
                    button.config(state=DISABLED)
                    button_t.config(state=DISABLED)
            input_1=StringVar()
            input_1.trace_add("write",update_button)
            input_2=StringVar()
            input_2.trace_add("write",update_button)
            input_3=StringVar()
            input_3.trace_add("write",update_button)
            input_4=StringVar()
            input_4.trace_add("write",update_button)
            input_5=StringVar()
            input_5.trace_add("write",update_button)
            input_6=StringVar() #stores the initial value
            input_6.trace_add("write",update_button)
            input_7=StringVar()#stores the steady state value
            input_7.trace_add("write",update_button)
            input_8=StringVar() #stores the initial value
            input_8.trace_add("write",update_button)
            input_9=StringVar()#stores the steady state value
            input_9.trace_add("write",update_button)
            my_labelR=Label(top,text='Enter value of equivalent resistance(in ohms):')
            my_labelR.grid(row=0,column=0) #input_1 is Req
            Entry(top,textvariable=input_1).grid(row=0,column=1,sticky=W+E)
            my_labelC=Label(top,text='Enter value of equivalent inductance(in henry):')
            my_labelC.grid(row=1,column=0) #input_2 is Leq
            Entry(top,textvariable=input_2).grid(row=1,column=1,sticky=W+E)
            mylabelV=Label(top,text="Enter value of voltage source(in volts): ")
            mylabelV.grid(row=2,column=0) #input_3 is Vsource
            Entry(top,textvariable=input_3).grid(row=2,column=1,sticky=W+E)
            mylabelV0=Label(top,text="Enter value of initial current across equivalent inductor(in amps): ")
            mylabelV0.grid(row=3,column=0) #input_4 is i(0)
            Entry(top,textvariable=input_4).grid(row=3,column=1,sticky=W+E)
            mylabelRu=Label(top,text="Choose a resistor from circuit to view its waveforms: ")
            mylabelRu.grid(row=4,column=0) #input_5 is selected R
            Entry(top,textvariable=input_5).grid(row=4,column=1,sticky=W+E)
            
            frame5=LabelFrame(top,padx=10,pady=10)

            def show(val): #in this window enter the value of inital conditions of resistor
                 val=clicked.get()
                 if val=="Amps":
                      global p 
                      p=val
                      frame5.grid_forget()
                      
                      frame5.grid(row=6,column=0)
                      Label(frame5,text='Initial value(in amps)').grid(row=0,column=0)
                      input_6.set("")
                      Entry(frame5,textvariable=input_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in amps)').grid(row=1,column=0)
                      input_7.set("")
                      Entry(frame5,textvariable=input_7).grid(row=1,column=1)
                      button.grid(row=7,column=0,pady=5)
                      button_t.grid(row=8,column=0,pady=5)
                 if val=="Volts":
                      p=val
                      frame5.grid_forget()
                      
                      frame5.grid(row=6,column=0)
                      Label(frame5,text='Initial value(in volts)').grid(row=0,column=0)
                      input_6.set("")
                      Entry(frame5,textvariable=input_6).grid(row=0,column=1)
                      Label(frame5,text='Steady state value(in volts)').grid(row=1,column=0)
                      input_7.set("")
                      Entry(frame5,textvariable=input_7).grid(row=1,column=1)
                      button.grid(row=7,column=0,pady=5)
                      button_t.grid(row=8,column=0,pady=5)
            Label(top,text='Enter initial and steady state values across selected resistor in units of').grid(row=5,column=0)
            drop=OptionMenu(top,clicked,"Amps","Volts",command=show)
            drop.config(width=20)
            drop.grid(row=5,column=1)
            def time_constantRL1(val1,val2,val3,val4): #val3 is current source val4 is initial condition
                plt.close("Resistor Voltage with no source")
                plt.close("Resistor Current with no source")
                global t
                global tau
                tau=float(val2)/float(val1)
                #print(tau)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<=1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,500,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                #voltage across capacitor
                
                #print(tau)
                #Label(top,text='Time constant(in seconds)= '+str(tau)).grid(row=6,column=0)
                I_L=(float(val3)*(1-np.exp(-t/tau)))/float(val1) +(float(val4)*np.exp(-t/tau))
                #print(type(V_C))
               
                #current across capacitor
                V_L=((float(val3)-(float(val1)*float(val4)))*np.exp(-t/tau))
                plt.figure("Inductor voltage")
                plt.plot(t,V_L,label='inductor voltage',color='blue')
                plt.ylabel('Voltage(in volts)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveforms of inductor voltage in transient analysis with external source connected')
                plt.legend()
                plt.figure("Inductor current")
                plt.plot(t,I_L,label='inductor current',color='red')
                plt.ylabel('Current(in amps)')
                plt.xlabel('Time(in seconds)')
                plt.title('Waveform of current through inductor in transient analysis with external source connected')
                plt.legend()
                plt.show()
            def resistanceRL1(val,val1,val2,val3,val4): #to plot voltage and current across resistor
                plt.close('Inductor voltage')
                plt.close('Inductor current')
                global t
                global tau
                #t=np.arange(0,10*3.14,0.01)
                tau=float(val4)/float(val3)
                if abs(tau)<0.00001: #tau less than 10 microseconds
                    t=np.linspace(0,0.00001,500)
                if abs(tau)>=0.00001 and abs(tau)<0.001:
                    t=np.linspace(0,0.0001*10,500,dtype=float)
                if abs(tau)>=0.001 and abs(tau)<1:
                    t=np.linspace(0,1,500)
                if abs(tau)>=1 and abs(tau)<100:
                    t=np.linspace(0,100,500)
                if abs(tau)>=100 and abs(tau)<500:
                    t=np.linspace(0,500,500)
                if abs(tau)>=500:
                    t=np.linspace(0,1000,500)
                if val=="Volts":
                     initial=float(val1)
                     steady_state=float(val2)
                     V_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor Voltage with source")
                     plt.plot(t,V_R,label='resistor voltage',color='green')
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Voltage(in volts)')
                     plt.title('Waveforms of voltage across '+input_5.get()+' ohm resistor with external source connected')
                     plt.legend()
                     plt.show()
                if val=="Amps":
                     initial=float(val1)
                     steady_state=float(val2)
                     I_R=steady_state + (initial-steady_state)*np.exp(-t/tau)
                     #plt.close()
                     plt.figure("Resistor Current with source")
                     plt.plot(t,I_R,label='resistor current',color='purple')
                     plt.xlabel('time(in seconds)')
                     plt.ylabel('Current(in amps)')
                     plt.title('Waveforms of current through '+input_5.get()+' ohm resistor with external source connected')
                     plt.legend()
                     plt.show()
            button=Button(top,text='Waveforms of the resistor selected',command=lambda:resistanceRL1(p,input_6.get(),input_7.get(),input_1.get(),input_2.get()),state=DISABLED)
            button.grid(row=6,column=0,columnspan=2,pady=5)
            button_t=Button(top,text='Waveforms of equivalent inductor',command=lambda:time_constantRL1(input_1.get(),input_2.get(),input_3.get(),input_4.get()),state=DISABLED)
            button_t.grid(row=7,column=0,columnspan=2,pady=5)
def display(value):
    global top
    global top1
    if top is not None:
         top.destroy()
    if top1 is not None:
         top1.destroy()
    if value == 'RL':
        frame2.grid_forget()
        frame1.grid_forget()
        frame3.grid_forget()
        plt.close('all')
        frame1.grid(row=2,column=0,columnspan=3)
        var2.set('None')
        Radiobutton(frame1,text='Without Source',variable=var2,value='RL0',command=lambda:window(var2.get())).grid(row=0,column=0)
        var2.set('None')
        Radiobutton(frame1,text='With Source',variable=var2,value='RL1',command=lambda:window(var2.get())).grid(row=1,column=0)
    elif value =='RC':
        frame1.grid_forget()
        frame2.grid_forget()
        frame3.grid_forget()
        plt.close('all')
        frame2.grid(row=2,column=0,columnspan=3)
        var2.set('None')
        Radiobutton(frame2,text='Without Source',variable=var2,value='RC0',command=lambda:window(var2.get())).grid(row=0,column=0)
        var2.set('None')
        Radiobutton(frame2,text='With Source',variable=var2,value='RC1',command=lambda:window(var2.get())).grid(row=1,column=0)
frame4=LabelFrame(root,text='Select the type of first order circuit: ')
frame4.grid(row=1,column=0,columnspan=3,pady=20,padx=20)  
Radiobutton(frame4,variable=var,text='RL',value='RL',command=lambda:display(var.get())).grid(row=0,column=0,padx=50)
Radiobutton(frame4,variable=var,text='RC',value='RC',command=lambda:display(var.get())).grid(row=0,column=1,padx=50)
#Radiobutton(frame4,variable=var,text='RLC',value='RLC',command=lambda:display(var.get())).grid(row=0,column=2,padx=10)
root.mainloop()