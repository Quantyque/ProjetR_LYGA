import React, { createContext, useContext, useEffect, useState, ReactNode } from 'react';

interface ToastContextProps {
  showToast: (message: string, type: string) => void;
  hideToast: () => void;
  toast: { message: string; type: string };
}

const ToastContext = createContext<ToastContextProps | undefined>(undefined);

interface ToastProviderProps {
  children: ReactNode;
}

export const ToastProvider: React.FC<ToastProviderProps> = ({ children }) => {
  const [toast, setToast] = useState({ message: '', type: '' });

  const showToast = (message: string, type: string) => {
    setToast({ message, type });

    localStorage.setItem('toastMessage', message);
    localStorage.setItem('toastType', type);

    setTimeout(() => {
      setToast({ message: '', type: '' });
      localStorage.removeItem('toastMessage');
      localStorage.removeItem('toastType');
    }, 3000);
  };

  const hideToast = () => {
    setToast({ message: '', type: '' });
  };

  useEffect(() => {
    const savedMessage = localStorage.getItem('toastMessage');
    const savedType = localStorage.getItem('toastType');

    if (savedMessage && savedType) {
      setToast({ message: savedMessage, type: savedType });

      setTimeout(() => {
        setToast({ message: '', type: '' });
        localStorage.removeItem('toastMessage');
        localStorage.removeItem('toastType');
      }, 3000);
    }
  }, []);

  return (
    <ToastContext.Provider value={{ showToast, hideToast, toast }}>
      {children}
    </ToastContext.Provider>
  );
};

export const useToast = () => {
  const context = useContext(ToastContext);

  if (!context) {
    throw new Error('useToast must be used within a ToastProvider');
  }

  return context;
};
