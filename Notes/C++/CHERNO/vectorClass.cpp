#include <iostream>
#include <vector>
#include <array>

template <typename T>
class Vector
{

        public:
                Vector() { 
                        // Allocate 2 Elements
                        ReAlloc(2);
                }

                void PushBack(const T& value)
                {
                        if(m_Size >= m_Capacity)
                                ReAlloc(m_Capacity + m_Capacity / 2);

                        m_Data[m_Size] = value;
                        m_Size++;
                }
                size_t Size()
                {
                        return m_Size;
                }
        const T& operator[](size_t index) const
        {
                if(index >= m_Size) { /* ASSERT */ }
                return m_Data[index];
        }

        T& operator[](size_t index)
        {
                if(index >= m_Size) { /* ASSERT  */ }

                return m_Data[index];
        }

        private:
                void ReAlloc(size_t newCapacity) {
                        // 1. Allocate a new block of memory
                        // 2. Copy/Move old elements into new block
                        // 3. Delete
                        
                        T* newBlock = new T[newCapacity];

                        if(newCapacity < m_Size)
                                m_Size = newCapacity;
                        for(size_t i = 0; i < m_Size; i++)
                                newBlock[i] = m_Data[i];

                        delete[] m_Data;
                        m_Data = newBlock;
                        m_Capacity = newCapacity;
                }

        private:
                T* m_Data = nullptr;
                size_t m_Size = 0;
                size_t m_Capacity = 0;

};

template<typename T>
void PrintVector(const Vector<T>& vector)
{
        for(size_t i = 0; i < vector.Size();i++)
                std::cout << vector[i] << std::endl;

        std::cout << "-------------------------\n";
}
int main()
{
        std::array<std::string,2> data;
        data[0] = "Captainchris";
        data[1] = "C++";

        Vector<std::string> vector;

        vector.PushBack("Captainchris");
        vector.PushBack("C++");
        vector.PushBack("Vector");
        vector.PushBack("Captainchris");
        
        PrintVector(vector);
        
        return 0;
}

