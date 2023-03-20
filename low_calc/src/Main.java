

public class Main
{
    public static String romanize(String num)
    {
        String romNum = "";
        int intNum = Integer.parseInt(num);
        if(intNum < 1)
        {
            throw new IllegalArgumentException();
        }
        if(intNum == 100)
        {
            romNum = "C";
            intNum = 0;
        }
        if(intNum >= 90)
        {
            romNum += "XC";
            intNum -= 90;
        }
        if(intNum >= 50)
        {
            romNum += "L";
            intNum -= 50;
        }
        if(intNum >= 40)
        {
            romNum += "XL";
            intNum -= 40;
        }
        while(intNum >= 10)
        {
            romNum += "X";
            intNum -= 10;
        }
        if(intNum == 9)
        {
            romNum += "IX";
            intNum = 0;
        }
        if(intNum >= 5)
        {
            romNum += "V";
            intNum -= 5;
        }
        if(intNum == 4)
        {
            romNum += "IV";
            intNum = 0;
        }
        while(intNum > 0)
        {
            romNum += "I";
            intNum -= 1;
        }
        return romNum;
    }

    public static int unromanize(String romNum)
    {
        int num = 0;
        switch(romNum)
        {
            case "I":
                num = 1;
                break;
            case "II":
                num = 2;
                break;
            case "III":
                num = 3;
                break;
            case "IV":
                num = 4;
                break;
            case "V":
                num = 5;
                break;
            case "VI":
                num = 6;
                break;
            case "VII":
                num = 7;
                break;
            case "VIII":
                num = 8;
                break;
            case "IX":
                num = 9;
                break;
            case "X":
                num = 10;
                break;
            default:
                throw new IllegalArgumentException();

        }
        return num;
    }

    public static String calc(String input)
    {
        String tInput = input;
        tInput = tInput.replaceAll("\\s","");
        boolean roman = false;
        char[] ops = {'+', '-', '/', '*'};
        if(tInput.matches("[IXV]+[-+*/][IXV]+"))
        {
            roman = true;
        }
        else if (tInput.matches("[123456789]+0*[-+*/][123456789]+0*"))
        {
            roman = false;
        }
        else
        {
            throw new IllegalArgumentException();
        }
        String num1 = "";
        String num2 = "";
        int intNum1;
        int intNum2;
        boolean numF = true;
        char action = '+';
        String result = "";
        for(char c: tInput.toCharArray())
        {
            boolean opF = false;
            for(char op:ops)
            {
                if(op == c)
                {
                    opF = true;
                    break;
                }
            }
            if(opF)
            {
                action = c;
                numF = false;
            }
            else
            {
                if(numF)
                {
                    num1 += c;
                }
                else
                {
                    num2 += c;
                }
            }
        }
        //System.out.println(num1);
        //System.out.println(num2);
        //System.out.println(roman);
        if(roman)
        {
            intNum1 = unromanize(num1);
            intNum2 = unromanize(num2);
        }
        else
        {
            intNum1 = Integer.parseInt(num1);
            intNum2 = Integer.parseInt(num2);
            if(intNum1 > 10 || intNum2 > 10)
            {
                throw new IllegalArgumentException();
            }
        }
        switch(action)
        {
            case '+':
                result = Integer.toString(intNum1 + intNum2);
                break;
            case '-':
                result = Integer.toString(intNum1 - intNum2);
                break;
            case '*':
                result = Integer.toString(intNum1 * intNum2);
                break;
            case '/':
                result = Integer.toString(intNum1 / intNum2);
                break;
        }
        if(roman)
        {
            result = romanize(result);
        }
        //System.out.println(result);
        return result;
    }
    public static void main(String[] args)
    {
        calc("1 + 2");
        calc("VI / III");
    }
}