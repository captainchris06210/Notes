#include <iostream>

class Log {
        public: 
                const int LogLevelError = 0;
                const int LogLevelWarning = 1;
                const int LogLevelInfo = 2;
        private:
                int m_LogLevel = LogLevelInfo;
        public:
                void SetLevel(int level) { m_LogLevel = level; }
                void Info(const char* message)
                {
                        if(m_LogLevel >= LogLevelInfo)
                                std::cout << "[INFO]: " << message << "\n";
                }
                void Warn(const char* message)
                {
                        if(m_LogLevel >= LogLevelWarning)
                                std::cout << "[WARNING]: " << message << "\n";
                }
                void Error(const char* message)
                {
                        if(m_LogLevel >= LogLevelError)
                             std::cout << "[ERROR]: " << message << "\n";
                }
};

int main()
{
        Log log;

        log.SetLevel(log.LogLevelWarning);
        log.Warn("Hello!");
        std::cin.get();
        return 0;
}
