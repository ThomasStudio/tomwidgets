class Emoji:
    class Flat:
        # ================ CORE SYMBOLS ================

        # Status Indicators
        Error = "⨯"            # (U+2A2F)
        Success = "✓"         # (U+2713) Thin checkmark

        # Checkmarks and Crosses
        Checkmark = "✓"        # (U+2713) Thin checkmark
        Cross = "✗"            # Thin cross

        # Basic Math Symbols
        Plus = "＋"            # Thin plus sign
        Minus = "－"           # Thin minus sign
        Multiply = "×"         # Multiplication sign
        Divide = "÷"           # Division sign
        Equal = "＝"           # Equals sign
        NotEqual = "≠"         # Not equal sign

        # ================ UI CONTROLS ================

        # Action Buttons
        Add = "➕"             # Add/Plus button
        Remove = "➖"          # Remove/Minus button
        Close = "✕"           # Close button
        Restore = "⤢"         # Restore button
        Pin = "📌"            # Pin button
        Lock = "🔒"           # Lock
        Unlock = "🔓"         # Unlock

        # Box Symbols
        Box = "☐"             # Empty box (U+2610)
        BoxChecked = "☑"      # Checked box (U+2611)
        BoxCross = "☒"        # Crossed box (U+2612)
        BoxQuestion = "⍰"     # Question box (U+2370)
        BoxDiagonal = "⧄"     # Diagonal box (U+29C4)

        # Boxed Math Symbols
        BoxPlus = "⊞"         # Boxed plus (U+229E)
        BoxMinus = "⊟"        # Boxed minus (U+229F)
        BoxTimes = "⊠"        # Boxed times (U+22A0)
        BoxDot = "⊡"          # Boxed dot (U+22A1)

        # Circle Symbols
        CirclePlus = "⊕"      # Circled plus (U+2295)
        CircleMinus = "⊖"     # Circled minus (U+2296)
        SquareInCircle = "⬤"  # Square in circle (U+2B24)

        # Radio Buttons
        RadioUnchecked = "○"  # Unchecked radio button
        RadioChecked = "◉"    # Checked radio button
        RadioDot = "⦿"        # Dotted radio button (U+29BF)

        # ================ MENU & NAVIGATION ================

        # Menu Icons
        Menu = "☰"            # Hamburger menu
        Menu2 = "≡"           # Three-line menu
        Menu3 = "⋮"           # Vertical three-dot menu
        Menu4 = "⋯"           # Horizontal three-dot menu
        MenuVertical = "▮"    # Vertical menu
        MenuHorizontal = "▬"  # Horizontal menu

        # Menu Actions
        MenuExpand = "▸"      # Menu expand
        MenuCollapse = "▾"    # Menu collapse
        MenuTree = "└"        # Tree menu
        MenuSub = "├"         # Sub-menu
        MenuToggleOn = "◼"    # Toggle on
        MenuToggleOff = "◻"   # Toggle off
        MenuIndent = "↳"      # Indent
        MenuOutdent = "↰"     # Outdent

        # ================ WINDOWS & LAYOUT ================

        WindowTile = "▦"      # Tile windows (U+25A6)
        WindowCascade = "▤"   # Cascade windows (U+25A4)

        # ================ ENCIRCLED CHARACTERS ================

        # Encircled Numbers
        Box0 = "⓪"            # (U+24EA)
        Box1 = "①"            # (U+2460)
        Box2 = "②"            # (U+2461)
        Box3 = "③"            # (U+2462)
        Box4 = "④"            # (U+2463)
        Box5 = "⑤"            # (U+2464)
        Box6 = "⑥"            # (U+2465)
        Box7 = "⑦"            # (U+2466)
        Box8 = "⑧"            # (U+2467)
        Box9 = "⑨"            # (U+2468)

        # Encircled Uppercase Letters
        BoxA = "Ⓐ"            # (U+24B6)
        BoxB = "Ⓑ"            # (U+24B7)
        BoxC = "Ⓒ"            # (U+24B8)
        BoxD = "Ⓓ"            # (U+24B9)
        BoxE = "Ⓔ"            # (U+24BA)
        BoxF = "Ⓕ"            # (U+24BB)
        BoxG = "Ⓖ"            # (U+24BC)
        BoxH = "Ⓗ"            # (U+24BD)
        BoxI = "Ⓘ"            # (U+24BE)
        BoxJ = "Ⓙ"            # (U+24BF)
        BoxK = "Ⓚ"            # (U+24C0)
        BoxL = "Ⓛ"            # (U+24C1)
        BoxM = "Ⓜ"            # (U+24C2)
        BoxN = "Ⓝ"            # (U+24C3)
        BoxO = "Ⓞ"            # (U+24C4)
        BoxP = "Ⓟ"            # (U+24C5)
        BoxQ = "Ⓠ"            # (U+24C6)
        BoxR = "Ⓡ"            # (U+24C7)
        BoxS = "Ⓢ"            # (U+24C8)
        BoxT = "Ⓣ"            # (U+24C9)
        BoxU = "Ⓤ"            # (U+24CA)
        BoxV = "Ⓥ"            # (U+24CB)
        BoxW = "Ⓦ"            # (U+24CC)
        BoxX = "Ⓧ"            # (U+24CD)
        BoxY = "Ⓨ"            # (U+24CE)
        BoxZ = "Ⓩ"            # (U+24CF)

        # Encircled Lowercase Letters
        Boxa = "ⓐ"            # (U+24D0)
        Boxb = "ⓑ"            # (U+24D1)
        Boxc = "ⓒ"            # (U+24D2)
        Boxd = "ⓓ"            # (U+24D3)
        Boxe = "ⓔ"            # (U+24D4)
        Boxf = "ⓕ"            # (U+24D5)
        Boxg = "ⓖ"            # (U+24D6)
        Boxh = "ⓗ"            # (U+24D7)
        Boxi = "ⓘ"            # (U+24D8)
        Boxj = "ⓙ"            # (U+24D9)
        Boxk = "ⓚ"            # (U+24DA)
        Boxl = "ⓛ"            # (U+24DB)
        Boxm = "ⓜ"            # (U+24DC)
        Boxn = "ⓝ"            # (U+24DD)
        Boxo = "ⓞ"            # (U+24DE)
        Boxp = "ⓟ"            # (U+24DF)
        Boxq = "ⓠ"            # (U+24E0)
        Boxr = "ⓡ"            # (U+24E1)
        Boxs = "ⓢ"            # (U+24E2)
        Boxt = "ⓣ"            # (U+24E3)
        Boxu = "ⓤ"            # (U+24E4)
        Boxv = "ⓥ"            # (U+24E5)
        Boxw = "ⓦ"            # (U+24E6)
        Boxx = "ⓧ"            # (U+24E7)
        Boxy = "ⓨ"            # (U+24E8)
        Boxz = "ⓩ"            # (U+24E9)

        # ================ ARROW SYMBOLS ================

        # Basic Arrows
        ArrowUp = "↑"
        ArrowDown = "↓"
        ArrowLeft = "←"
        ArrowRight = "→"
        ArrowUpDown = "↕"
        ArrowLeftRight = "↔"
        ArrowReturn = "↲"
        ArrowEnter = "↵"

        # Diagonal Arrows
        ArrowNortheast = "↗"
        ArrowNorthwest = "↖"
        ArrowSoutheast = "↘"
        ArrowSouthwest = "↙"

        # Rotating Arrows
        ArrowLoop = "↺"
        ArrowRotate = "↻"
        ArrowArc = "↶"
        ArrowCurve = "↷"
        ArrowWave = "↝"
        ArrowZigzag = "↯"

        # ================ FORM CONTROLS ================

        TextField = "⎕"
        TextArea = "▯"
        Dropdown = "▾"
        Combobox = "▽"
        Slider = "▬"
        Range = "▭"
        Spinner = "⌾"
        DatePicker = "📅"
        TimePicker = "🕐"
        ColorPicker = "🎨"
        FileUpload = "📎"

        # ================ DIRECTIONAL NAVIGATION ================

        North = "⬆️"
        South = "⬇️"
        East = "➡️"
        West = "⬅️"
        Northeast = "⬈"
        Northwest = "⬉"
        Southeast = "⬊"
        Southwest = "⬋"

        # Navigation Icons
        CompassRose = "✜"
        Target = "◎"
        Waypoint = "⛯"
        Location = "⌖"
        MapPin = "📍"
        Route = "⇄"
        Merge = "⇉"
        Fork = "⇈"
        Junction = "⨀"
        Intersection = "⨂"

        # ================ PAGE NAVIGATION ================

        PageUp = "⇞"
        PageDown = "⇟"
        Top = "⤒"
        Bottom = "⤓"

        # Pagination Icons
        FirstPage = "⏮"
        LastPage = "⏭"
        PrevPage = "◀"
        NextPage = "▶"
        PageFirst = "⏪"
        PageLast = "⏩"
        PageNumber = "№"
        BookmarkPage = "🔖"
        TableOfContents = "📑"
        Index = "🔍"
        BookOpen = "📖"
        BookClosed = "📕"

        # ================ UI CONTROLS ================

        Resize = "⤡"
        FlipHorizontal = "⇄"
        FlipVertical = "⇅"
        ZoomReset = "⨀"
        Pan = "✥"
        Drag = "⤢"
        Drop = "⤓"
        Grab = "☚"
        Hand = "☛"
        Cursor = "▸"
        Pointer = "☞"
        IBeam = "|"
        Crosshair = "⨁"
        Wait = "⌛"
        Working = "⚙"

        # ================ CONTEXT MENU ================

        RightClick = "🖱️"
        Touch = "👆"
        Tap = "•"
        LongPress = "••"
        DoubleTap = "••"
        Pinch = "🤏"
        Spread = "✌️"

        # ================ ACTION ICONS ================

        Execute = "▶"
        Run = "▷"
        Stop = "■"
        Pause = "⏸"
        Resume = "⏵"
        StepInto = "⤵"
        StepOver = "⤴"
        StepOut = "⤶"
        Breakpoint = "●"
        Debug = "🐛"
        Profile = "📊"
        Benchmark = "⏱"
        Optimize = "⚡"
        Build = "🔨"
        Deploy = "🚀"
        Install = "📦"
        Update = "🔄"
        Upgrade = "⬆"
        Downgrade = "⬇"

        # ================ FILE OPERATIONS ================

        FileRename = "✏"
        FileDuplicate = "📄"
        FileCopy = "📋"
        FileMove = "➡"
        FileDelete = "🗑"
        FileArchive = "📦"
        FileExtract = "📤"
        FileCompress = "🗜"
        FileBackup = "💾"
        FileCompare = "⇔"
        FileMerge = "⇉"
        FileDiff = "≠"
        FileInfo = "ℹ"

        # ================ EDITING OPERATIONS ================

        EditFind = "🔍"
        EditFind2= "🔎"
        EditReplace = "⇄"
        EditFindNext = "⤵"
        EditFindPrev = "⤴"
        EditGoTo = "➡"
        EditComment = "💬"
        EditUncomment = "🚫"
        EditFormat = "🔤"
        EditCaseUpper = "A"
        EditCaseLower = "a"
        EditCaseTitle = "T"
        EditWrap = "↩"
        EditJoin = "⇥"
        EditSplit = "⇤"
        EditShuffle = "🔀"

        # ================ BOX DRAWING ================

        # Light Box Drawing
        BoxLightHorizontal = "─"
        BoxLightVertical = "│"
        BoxLightDownRight = "┌"
        BoxLightDownLeft = "┐"
        BoxLightUpRight = "└"
        BoxLightUpLeft = "┘"
        BoxLightCross = "┼"
        BoxLightTeeRight = "├"
        BoxLightTeeLeft = "┤"
        BoxLightTeeDown = "┬"
        BoxLightTeeUp = "┴"

        # Double Line Box Drawing
        BoxLightDoubleHorizontal = "═"
        BoxLightDoubleVertical = "║"
        BoxLightDoubleDownRight = "╔"
        BoxLightDoubleDownLeft = "╗"
        BoxLightDoubleUpRight = "╚"
        BoxLightDoubleUpLeft = "╝"
        BoxLightDoubleCross = "╬"
        BoxLightDoubleTeeRight = "╠"
        BoxLightDoubleTeeLeft = "╣"
        BoxLightDoubleTeeDown = "╦"
        BoxLightDoubleTeeUp = "╩"

        # Heavy Box Drawing
        BoxHeavyHorizontal = "━"
        BoxHeavyVertical = "┃"
        BoxHeavyDownRight = "┏"
        BoxHeavyDownLeft = "┓"
        BoxHeavyUpRight = "┗"
        BoxHeavyUpLeft = "┛"
        BoxHeavyCross = "╋"
        BoxHeavyTeeRight = "┣"
        BoxHeavyTeeLeft = "┫"
        BoxHeavyTeeDown = "┳"
        BoxHeavyTeeUp = "┻"

        # Rounded Box Drawing
        BoxRoundedDownRight = "╭"
        BoxRoundedDownLeft = "╮"
        BoxRoundedUpRight = "╰"
        BoxRoundedUpLeft = "╯"

        # Diagonal and Shadow Box Drawing
        BoxDiagonalDownRight = "╱"
        BoxDiagonalDownLeft = "╲"
        BoxDiagonalCross = "╳"
        BoxShadowLight = "░"
        BoxShadowMedium = "▒"
        BoxShadowHeavy = "▓"
        BoxSolid = "█"

        # ================ MUSIC SYMBOLS ================

        MusicNote = "♪"
        MusicNotes = "♫"
        Sharp = "♯"
        Flat = "♭"
        Natural = "♮"

        # ================ ACTION & CONTROL ================

        Sort = "⇅"
        Expand = "⯈"
        Collapse = "⯆"

    class Position:
        Left = "←"          # (U+2190)
        Right = "→"         # (U+2192)
        Top = "↑"           # (U+2191)
        Bottom = "↓"        # (U+2193)

        TopLeft = "↖"       # (U+2196)
        TopRight = "↗"      # (U+2197)
        BottomLeft = "↙"    # (U+2199)
        BottomRight = "↘"   # (U+2198)

        TopLeft2 = "◤"  # (U+25E4)
        TopRight2 = "◥"  # (U+25E5)
        BottomLeft2 = "◣"  # (U+25E3)
        BottomRight2 = "◢"  # (U+25E2)

        # UI alignment
        AlignCenterHorizontal = "↔"  # (U+2194)
        AlignCenterVertical = "↕"   # (U+2195)

        # border position
        BorderTopLeft = "┌"         # (U+250C)
        BorderTopRight = "┐"        # (U+2510)
        BorderBottomLeft = "└"      # (U+2514)
        BorderBottomRight = "┘"     # (U+2518)

        # pointer position
        PointerLeft = "☚"           # (U+261A)
        PointerRight = "☛"          # (U+261B)
        PointerUp = "☝"             # (U+261D)
        PointerDown = "☟"           # (U+261F)

        # triangle position
        TriangleLeft = "◀"          # (U+25C0)
        TriangleRight = "▶"         # (U+25B6)
        TriangleUp = "▲"            # (U+25B2)
        TriangleDown = "▼"          # (U+25BC)

        # small triangle position
        SmallTriangleLeft = "◂"     # (U+25C2)
        SmallTriangleRight = "▸"    # (U+25B8)
        SmallTriangleUp = "▴"       # (U+25B4)
        SmallTriangleDown = "▾"     # (U+25BE)

        # hollow triangle position
        TriangleLeftOutline = "◁"   # (U+25C1)
        TriangleRightOutline = "▷"  # (U+25B7)
        TriangleUpOutline = "△"     # (U+25B3)
        TriangleDownOutline = "▽"   # (U+25BD)

        # circle position
        CircleTop = "◴"  # (U+25F4)
        CircleRight = "◵"  # (U+25F5)
        CircleBottom = "◶"  # (U+25F6)
        CircleLeft = "◷"  # (U+25F7)

        # cross position
        CrossTop = "⊥"              # (U+22A5)
        CrossBottom = "⊤"           # (U+22A4)
        CrossLeft = "⊣"             # (U+22A3)
        CrossRight = "⊢"            # (U+22A2)
        CrossCenter = "✚"           # (U+271A)

        # grid position
        GridTopLeft = "┌"           #
        GridTopCenter = "┬"         # (U+252C)
        GridTopRight = "┐"          #
        GridMiddleLeft = "├"        # (U+251C)
        GridMiddleCenter = "┼"      #
        GridMiddleRight = "┤"       # (U+2524)
        GridBottomLeft = "└"        #
        GridBottomCenter = "┴"      # (U+2534)
        GridBottomRight = "┘"       #

        # coordinate position
        Origin = "⨁"               # (U+2A01)
        XAxis = "→"
        YAxis = "↑"
        Quadrant1 = "↗"
        Quadrant2 = "↖"
        Quadrant3 = "↙"
        Quadrant4 = "↘"

        # compass direction
        CompassNorth = "N"
        CompassSouth = "S"
        CompassEast = "E"
        CompassWest = "W"
        CompassRose = "✜"        # (U+271C)

        # layout position
        LayoutTop = "⬆"
        LayoutBottom = "⬇"
        LayoutLeft = "⬅"
        LayoutRight = "➡"
        LayoutCenter = "⦾"        # (U+29BE)

        # scroll indicator
        ScrollTop = "⤒"
        ScrollBottom = "⤓"
        ScrollLeft = "⇤"
        ScrollRight = "⇥"

        # table position
        TableTopLeft = "┌"
        TableTopRight = "┐"
        TableBottomLeft = "└"
        TableBottomRight = "┘"
        TableHeaderLeft = "├"
        TableHeaderRight = "┤"
        TableRowLeft = "├"
        TableRowRight = "┤"

        # text align
        TextAlignLeft = "←"
        TextAlignRight = "→"
        TextAlignCenter = "↔"
        TextAlignJustify = "⇔"      # (U+21D4)
        TextAlignTop = "↑"
        TextAlignBottom = "↓"
        TextAlignMiddle = "↕"

        # image crop position
        ImageCropTopLeft = "┌"
        ImageCropTopRight = "┐"
        ImageCropBottomLeft = "└"
        ImageCropBottomRight = "┘"
        ImageCropCenter = "⨁"

        # map pin position
        MapPinNorth = "📍↑"
        MapPinSouth = "📍↓"
        MapPinEast = "📍→"
        MapPinWest = "📍←"

        # cursor block position
        CursorBlockTop = "▀"        # (U+2580)
        CursorBlockBottom = "▄"     # (U+2584)
        CursorBlockLeft = "▌"       # (U+258C)
        CursorBlockRight = "▐"      # (U+2590)

        # special position marker
        MarkerCenter = "⦿"          # (U+29BF)
        MarkerCorner = "⛶"          # (U+26F6)

        # screen position
        ScreenTop = "▀"  # (U+2580)
        ScreenBottom = "▄"  # (U+2584)
        ScreenLeft = "▌"  # (U+258C)
        ScreenRight = "▐"  # (U+2590)
        ScreenTopLeft = "▘"  # (U+2598)
        ScreenTopRight = "▝"  # (U+259D)
        ScreenBottomLeft = "▖"  # (U+2596)
        ScreenBottomRight = "▗"  # (U+2597)
        ScreenCenter = "▣"  # (U+25A3)

        # enhanced
        LeftThick = "⇐"          # (U+21D0)
        LeftThick2 = "⇦"
        RightThick = "⇒"         # (U+21D2)
        RightThick = "⇨"
        UpThick = "⇑"            # (U+21D1)
        DownThick = "⇓"          # (U+21D3)
        LeftRightThick = "⇔"    # (U+21D4)
        UpDownThick = "⇕"        # (U+21D5)

    # Navigation Arrows
    Home = "🏠"
    Back = "⬅️"
    Forward = "➡️"
    Up = "⬆️"
    Down = "⬇️"
    UpDown = "↕️"
    LeftRight = "↔️"

    # Action & Control
    Refresh = "🔄"
    Search = "🔍"
    Settings = "⚙️"
    Filter = "🔍"

    # File Operations
    FileNew = "➕"
    FileOpen = "📂"
    FileSave = "💾"
    FileSaveAs = "📥"
    FileClose = "❌"
    FilePrint = "🖨️"
    FileExport = "📤"
    FileImport = "📥"

    # Editing Operations
    EditCut = "✂"
    EditCopy = "📋"
    EditPaste = "📝"
    EditDelete = "🗑️"
    EditClear = "🧹"
    EditSelectAll = "📄"

    # Editing Operations
    EditUndo = "↩️"
    EditRedo = "↪️"

    # Formatting
    FormatBold = "𝐁"
    FormatItalic = "𝐼"
    FormatUnderline = "𝐔"
    FormatStrikethrough = "𝐒"
    FormatColor = "🎨"
    FormatAlignLeft = "⬅️"
    FormatAlignCenter = "⏺️"
    FormatAlignRight = "➡️"
    FormatAlignJustify = "↔️"
    FormatFont = "🔤"
    FormatSize = "📏"
    Format = "𝐅"

    # Folder operations
    FolderNew = "📁"
    FolderOpen = "📂"
    FolderClose = "📁"
    FolderSync = "🔄"
    FolderShare = "📤"
    FolderLock = "🔒"
    FolderUnlock = "🔓"
    FolderFavorite = "⭐"
    FolderRecent = "🕐"
    FolderStarred = "★"
    FolderTagged = "🏷"
    FolderArchive = "📦"

    # Status & Indicators
    Success = "✅"
    Error = "❌"
    Warning = "⚠️"
    Info = "ℹ️"
    Question = "❓"
    Loading = "⏳"
    Progress = "📊"
    Complete = "🏁"

    # View & Display
    ViewZoomIn = "🔍➕"
    ViewZoomOut = "🔍➖"
    ViewFullscreen = "⛶"
    ViewGrid = "🔲"
    ViewList = "📋"
    ViewDetails = "📊"
    ViewPreview = "👁️"

    # Tools & Utilities
    ToolCalculator = "🧮"
    ToolCalendar = "📅"
    ToolClock = "⏰"
    ToolRuler = "📐"
    ToolPaint = "🖌️"
    ToolEraser = "🧽"
    ToolCrop = "✂️"
    ToolRotate = "🔄"

    # Help & Support
    HelpAbout = "ℹ️"
    HelpDocumentation = "📖"
    HelpTutorial = "🎓"
    HelpSupport = "🆘"
    HelpFeedback = "💬"
    HelpBug = "🐛"
    HelpUpdate = "🔄"

    # Time & Calendar
    Clock = "🕐"
    Calendar = "📅"
    Stopwatch = "⏱️"
    Timer = "⏲️"
    Hourglass = "⏳"

    # Time and calendar
    ClockOne = "🕐"
    ClockTwo = "🕑"
    ClockThree = "🕒"
    ClockFour = "🕓"
    ClockFive = "🕔"
    ClockSix = "🕕"
    ClockSeven = "🕖"
    ClockEight = "🕗"
    ClockNine = "🕘"
    ClockTen = "🕙"
    ClockEleven = "🕚"
    ClockTwelve = "🕛"
    AlarmClock = "⏰"
    MantelpieceClock = "🕰"
    Watch = "⌚"
    PocketWatch = "⌚"
    TimerClock = "⏲"
    StopwatchClock = "⏱"
    HourglassFlowingSand = "⏳"
    HourglassDone = "⌛"
    CalendarDay = "📅"
    CalendarWeek = "🗓"
    CalendarMonth = "📆"
    CalendarYear = "📅"
    TearOffCalendar = "📅"
    Schedule = "📅"
    Agenda = "📋"
    Timeline = "⏳"
    History = "🕰"
    Future = "🚀"
    Past = "🕰"
    Present = "⏳"
    Deadline = "⏰"
    Reminder = "⏰"
    Notification = "🔔"
    Event = "📅"
    Meeting = "👥"
    Appointment = "📅"
    Birthday = "🎂"
    Holiday = "🎉"
    Vacation = "🏖"
    Workday = "💼"
    Weekend = "🌴"

    # Development & Code
    Code = "💻"
    Bug = "🐛"
    Terminal = "💻"
    Database = "🗄️"
    Server = "🖥️"
    Network = "🌐"
    Security = "🔒"

    # Communication
    Email = "📧"
    Message = "💬"
    Chat = "💭"
    Phone = "📞"
    VideoCall = "📹"
    AudioCall = "🎤"
    Share = "📤"

    # Status & Indicators (already in Flat)

    # Media & Content
    Image = "🖼️"
    Video = "🎬"
    Audio = "🎵"
    Document = "📄"
    Folder = "📁"
    Archive = "📦"
    Book = "📚"
    Music = "🎶"

    # User Interface
    User = "👤"
    Users = "👥"
    Lock = "🔒"
    Unlock = "🔓"
    Key = "🔑"
    Star = "⭐"  # Note: This is different from Flat.Star = "★"
    Heart = "❤️"  # Note: This is different from Flat.Heart = "♥"
    Bookmark = "🔖"

    # Navigation & Directions
    Previous = "⏮️"
    Next = "⏭️"
    First = "⏪"
    Last = "⏩"
    Play = "▶️"
    Pause = "⏸️"
    Stop = "⏹️"
    Record = "⏺️"

    # Miscellaneous
    Lightbulb = "💡"
    Gift = "🎁"
    Flag = "🚩"
    Trophy = "🏆"
    Medal = "🏅"
    Crown = "👑"
    Fire = "🔥"
    Water = "💧"

    # Weather & Time
    Sun = "☀️"
    Moon = "🌙"
    Cloud = "☁️"
    Rain = "🌧️"
    Snow = "❄️"
    Wind = "💨"
    Temperature = "🌡️"

    # Office & Business
    Briefcase = "💼"
    Chart = "📈"
    Graph = "📊"
    Presentation = "📽️"
    Meeting = "👥"

    # Food & Drink
    Coffee = "☕"
    Tea = "🍵"
    Pizza = "🍕"
    Burger = "🍔"
    Cake = "🍰"

    # Transportation
    Car = "🚗"
    Bus = "🚌"
    Train = "🚆"
    Plane = "✈️"
    Ship = "🚢"

    # Technology
    Computer = "💻"
    Phone = "📱"
    Tablet = "📱"
    Camera = "📷"
    Headphones = "🎧"

    # Sports & Games
    Basketball = "🏀"
    Football = "⚽"
    Tennis = "🎾"
    Chess = "♟️"
    Dice = "🎲"

    # Education
    BookOpen = "📖"
    Pencil = "✏️"
    Pen = "🖊️"
    Ruler = "📏"
    Graduation = "🎓"

    # Health & Medical
    Heartbeat = "💓"
    Pill = "💊"
    Syringe = "💉"
    Hospital = "🏥"
    Ambulance = "🚑"

    # Nature & Animals
    Tree = "🌳"
    Flower = "🌸"
    Leaf = "🍃"
    Cat = "🐱"
    Dog = "🐶"

    # Household
    House = "🏠"
    Building = "🏢"
    Factory = "🏭"
    Store = "🏪"
    Bank = "🏦"

    # Communication
    Envelope = "✉️"
    Mailbox = "📮"
    Megaphone = "📢"
    Bell = "🔔"
    Radio = "📻"

    # Security
    Shield = "🛡️"
    Keyhole = "🗝️"
    Fingerprint = "🖐️"
    Eye = "👁️"

    # Shopping
    ShoppingCart = "🛒"
    PriceTag = "🏷️"
    Barcode = "📊"
    CreditCard = "💳"

    # Entertainment
    TV = "📺"
    Movie = "🎬"
    Game = "🎮"
    MusicPlayer = "🎵"

    # Travel
    Map = "🗺️"
    Compass = "🧭"
    Suitcase = "🧳"
    Passport = "📘"

    # Science
    Microscope = "🔬"
    Telescope = "🔭"
    Atom = "⚛️"
    DNA = "🧬"

    # Art & Creativity
    Paintbrush = "🖌️"
    Palette = "🎨"
    Camera = "📸"
    Film = "🎞️"

    # Miscellaneous Icons
    Rocket = "🚀"
    Satellite = "🛰️"
    UFO = "🛸"
    Robot = "🤖"
    Alien = "👽"
    Ghost = "👻"
    Skull = "💀"
    Poop = "💩"


""" more emoji categories

        # Formatting
        FormatSubscript = "ₓ"
        FormatSuperscript = "ˣ"
        FormatCode = "</>"
        FormatQuote = "❝"
        FormatListBullet = "•"
        FormatListNumber = "1."
        FormatListCheck = "✓"
        FormatIndent = "↳"
        FormatOutdent = "↰"
        FormatLineHeight = "↕"
        FormatLetterSpacing = "⇔"
        FormatWordSpacing = "␣"
        FormatParagraph = "¶"
        FormatClear = "×"
        FormatReset = "↺"
        FormatPreset = "💾"
        FormatTemplate = "📄"

        # View & Display
        ViewZoomIn = "🔍➕"
        ViewZoomOut = "🔍➖"
        ViewFullscreen = "⛶"
        ViewGrid = "🔲"
        ViewList = "📋"
        ViewDetails = "📊"
        ViewPreview = "👁️"

        # View modes
        ViewThumbnail = "🖼"
        ViewTile = "▦"
        ViewCard = "🗂"
        ViewTimeline = "⏱"
        ViewCalendar = "📅"
        ViewGantt = "📊"
        ViewKanban = "📋"
        ViewMindmap = "🧠"
        ViewOutline = "📑"
        ViewSplit = "⇆"
        ViewDual = "⇄"
        ViewTriple = "⇉"
        ViewQuad = "⇶"
        ViewStack = "🗂"
        ViewCarousel = "↻"
        ViewSlide = "▯"
        ViewPage = "📄"
        ViewPrint = "🖨"
        ViewExport = "📤"

        # Tools & Utilities
        ToolCalculator = "🧮"
        ToolCalendar = "📅"
        ToolClock = "⏰"
        ToolRuler = "📐"
        ToolPaint = "🖌️"
        ToolEraser = "🧽"
        ToolCrop = "✂️"
        ToolRotate = "🔄"

        # Tools
        ToolSelect = "☐"
        ToolLasso = "🔄"
        ToolMagicWand = "✨"
        ToolClone = "⎘"
        ToolHeal = "❤️"
        ToolBrush = "🖌"
        ToolPencil = "✏"
        ToolPen = "🖊"
        ToolMarker = "🖍"
        ToolSpray = "💨"
        ToolBucket = "🪣"
        ToolGradient = "🌈"
        ToolText = "T"
        ToolShape = "◯"
        ToolLine = "─"
        ToolCurve = "⌒"
        ToolPolygon = "⬢"
        ToolStar = "☆"
        ToolSpiral = "🌀"
        ToolGrid = "▦"
        ToolGuide = "║"
        ToolMeasure = "📏"
        ToolEyeDropper = "👁"

        # Status indicators
        Pending = "⏳"
        Queued = "⏱"
        Processing = "⚙"
        Uploading = "📤"
        Downloading = "📥"
        Syncing = "🔄"
        Connecting = "🔗"
        Connected = "✓"
        Disconnected = "✗"
        Online = "🟢"
        Offline = "🔴"
        Idle = "⏸"
        Active = "▶"
        Busy = "⏳"
        Away = "⏱"
        DoNotDisturb = "🚫"
        Invisible = "👻"
        Hidden = "👁"
        Visible = "👁"
        Locked = "🔒"
        Unlocked = "🔓"
        Secured = "🛡"
        Verified = "✓"
        Unverified = "?"
        Beta = "β"
        Alpha = "α"
        Experimental = "⚗"
        Deprecated = "⏳"
        Legacy = "🕰"
        New = "🆕"
        Updated = "🔄"
        Hot = "🔥"
        Trending = "📈"
        Popular = "⭐"
        Featured = "🌟"
        Recommended = "👍"
        Favorite = "❤"
        Bookmarked = "🔖"
        Flagged = "🚩"
        Reported = "⚠"

        # Help & Support
        HelpAbout = "ℹ️"
        HelpDocumentation = "📖"
        HelpTutorial = "🎓"
        HelpSupport = "🆘"
        HelpFeedback = "💬"
        HelpBug = "🐛"
        HelpUpdate = "🔄"

        # Help and support
        HelpFAQ = "❓"
        HelpForum = "💬"
        HelpCommunity = "👥"
        HelpContact = "📞"
        HelpChat = "💭"
        HelpEmail = "📧"
        HelpPhone = "📱"
        HelpVideo = "🎬"
        HelpWalkthrough = "👣"
        HelpHint = "💡"
        HelpTip = "💡"
        HelpGuide = "🗺"
        HelpManual = "📕"
        HelpReference = "📚"
        HelpApi = "</>"
        HelpSample = "📄"
        HelpDemo = "🎬"
        HelpSandbox = "🏖"
        HelpPlayground = "🎪"

        # Development & Code
        Code = "💻"
        Bug = "🐛"
        Terminal = "💻"
        Database = "🗄️"
        Server = "🖥️"
        Network = "🌐"
        Security = "🔒"

        # Development and code
        Variable = "𝑥"
        Function = "ƒ"
        Class = "C"
        Interface = "I"
        Enum = "E"
        Struct = "S"
        Namespace = "⎔"
        Module = "📦"
        Package = "📦"
        Library = "📚"
        Framework = "🏗"
        Plugin = "🔌"
        Extension = "🔌"
        Theme = "🎨"
        Widget = "▦"
        Component = "⎔"
        Service = "⚙"
        Api = "</>"
        Sdk = "🛠"
        Git = "🐙"
        Branch = "🌿"
        Commit = "💾"
        Merge = "⇉"
        PullRequest = "📥"
        Issue = "🐛"
        Milestone = "🎯"
        Project = "📋"
        Board = "📊"
        Pipeline = "⛓"
        Workflow = "🔄"
        Job = "⚙"
        Stage = "⬢"
        Environment = "🌍"
        Container = "📦"
        Image = "🖼"
        Registry = "🗄"
        Orchestration = "🎼"
        Monitor = "📊"
        Log = "📝"
        Trace = "🔍"
        Metric = "📈"
        Alert = "🚨"
        Dashboard = "📊"
        Report = "📄"
        Analytics = "📊"

        # Miscellaneous
        Lightbulb = "💡"
        Gift = "🎁"
        Flag = "🚩"
        Trophy = "🏆"
        Medal = "🏅"
        Crown = "👑"
        Fire = "🔥"
        Water = "💧"

        # other
        Idea = "💡"
        Innovation = "✨"
        Inspiration = "🌟"
        Discovery = "🔍"
        Invention = "⚙"
        Solution = "✓"
        Problem = "❓"
        Challenge = "🎯"
        Goal = "🏁"
        Target = "🎯"
        Achievement = "🏆"
        Award = "🏅"
        Prize = "🎁"
        Reward = "⭐"
        Badge = "🛡"
        Certificate = "📜"
        Diploma = "📜"
        License = "📜"
        Contract = "📝"
        Agreement = "🤝"
        Deal = "🤝"
        Partnership = "🤝"
        Collaboration = "👥"
        Teamwork = "👥"
        Meeting = "👥"
        Conference = "🗣"
        Webinar = "🎬"
        Workshop = "🛠"
        Training = "🎓"
        Education = "🎓"
        Learning = "📚"
        Knowledge = "🧠"
        Wisdom = "👁"
        Experience = "⏳"
        Skill = "🛠"
        Talent = "⭐"
        Expert = "👨‍🎓"
        Professional = "👔"
        Career = "📈"
        Job = "💼"
        Work = "🛠"
        Business = "🏢"
        Enterprise = "🏭"
        Startup = "🚀"
        Company = "🏢"
        Organization = "🏛"
        Institution = "🏛"
        Government = "🏛"
        Nonprofit = "❤"
        Charity = "❤"
        Volunteer = "🤝"
        Donation = "💸"
        Fundraising = "💰"
        Investment = "📈"
        Finance = "💰"
        Banking = "🏦"
        Insurance = "🛡"
        Legal = "⚖"
        Compliance = "✓"
        Regulation = "📜"
        Policy = "📜"
        Terms = "📜"
        Privacy = "👁"
        Security = "🔒"
        Safety = "🛡"
        Health = "❤"
        Wellness = "🌿"
        Fitness = "🏃"
        Nutrition = "🍎"
        Medical = "🏥"
        Hospital = "🏥"
        Clinic = "🏥"
        Pharmacy = "💊"
        Laboratory = "⚗"
        Research = "🔬"
        Science = "🧪"
        Technology = "💻"
        Engineering = "⚙"
        Mathematics = "Σ"
        Physics = "⚛"
        Chemistry = "🧪"
        Biology = "🧬"
        Geology = "🌋"
        Astronomy = "⭐"
        Space = "🚀"
        Universe = "🌌"

        # weather
        WeatherSunny = "☀"
        WeatherPartlyCloudy = "⛅"
        WeatherCloudy = "☁"
        WeatherRainy = "🌧"
        WeatherStormy = "⛈"
        WeatherSnowy = "❄"
        WeatherWindy = "💨"
        WeatherFoggy = "🌫"
        WeatherHumid = "💦"
        WeatherDry = "🏜"
        WeatherHot = "🔥"
        WeatherCold = "❄"
        WeatherTemperature = "🌡"
        WeatherPressure = "📊"
        WeatherWindSpeed = "💨"
        WeatherSunrise = "🌅"
        WeatherSunset = "🌇"
        WeatherMoon = "🌙"
        WeatherStars = "⭐"
        WeatherRainbow = "🌈"
        WeatherTornado = "🌪"
        WeatherHurricane = "🌀"
        WeatherEarthquake = "🌋"
        WeatherFlood = "🌊"
        WeatherDrought = "🏜"
        WeatherSeasonSpring = "🌸"
        WeatherSeasonSummer = "☀"
        WeatherSeasonAutumn = "🍂"
        WeatherSeasonWinter = "❄"
        NatureTree = "🌳"
        NatureFlower = "🌸"
        NatureLeaf = "🍃"
        NatureGrass = "🌿"
        NatureBush = "🌳"
        NatureForest = "🌲"
        NatureMountain = "⛰"
        NatureHill = "⛰"
        NatureValley = "🏞"
        NatureRiver = "🌊"
        NatureLake = "🏞"
        NatureOcean = "🌊"
        NatureIsland = "🏝"
        NatureDesert = "🏜"
        NatureArctic = "❄"
        NatureTropical = "🌴"
        NatureSavanna = "🌾"
        NatureJungle = "🌴"
        NatureCave = "🕳"
        NatureVolcano = "🌋"
        NatureGlacier = "🏔"


        # Mathematical operations
        PlusMinus = "±"
        MinusPlus = "∓"
        Approximately = "≈"
        Proportional = "∝"
        Infinity = "∞"
        Null = "∅"
        ElementOf = "∈"
        NotElementOf = "∉"
        Subset = "⊂"
        Superset = "⊃"
        Union = "∪"
        Intersection = "∩"
        LogicalAnd = "∧"
        LogicalOr = "∨"
        LogicalNot = "¬"
        ForAll = "∀"
        Exists = "∃"
        Therefore = "∴"
        Because = "∵"
        Angle = "∠"
        RightAngle = "∟"
        Degree = "°"
        Prime = "′"
        DoublePrime = "″"
        Integral = "∫"
        DoubleIntegral = "∬"
        TripleIntegral = "∭"
        ContourIntegral = "∮"
        Summation = "∑"
        Product = "∏"
        Coproduct = "∐"
        Gradient = "∇"
        Laplacian = "∆"
        Partial = "∂"
        Nabla = "∇"

        # Geometric Shapes
        Circle = "●"
        Square = "■"
        Triangle = "▲"
        Diamond = "◆"
        Star = "★"
        Heart = "♥"
        Spade = "♠"
        Club = "♣"

        # Geometric shapes
        CircleOutline = "○"
        SquareOutline = "□"
        TriangleOutline = "△"
        DiamondOutline = "◇"
        StarOutline = "☆"
        HeartOutline = "♡"
        SpadeOutline = "♤"
        ClubOutline = "♧"
        Rectangle = "▭"
        RectangleOutline = "▯"
        Ellipse = "⬭"
        EllipseOutline = "⬯"
        Pentagon = "⬟"
        Hexagon = "⬢"
        Heptagon = "⬡"
        Octagon = "⯄"
        Parallelogram = "▰"
        Trapezoid = "⏢"
        Rhombus = "◆"
        Cube = "⬛"
        Sphere = "●"
        Cone = "▵"
        Cylinder = "⏢"
        Pyramid = "∆"
        Torus = "⭕"

        # Mathematical Symbols
        Infinity = "∞"
        Pi = "π"
        Sum = "∑"
        Product = "∏"
        Integral = "∫"
        Partial = "∂"
        Nabla = "∇"
        ForAll = "∀"

        # Mathematical symbols
        Alpha = "α"
        Beta = "β"
        Gamma = "γ"
        Delta = "δ"
        Epsilon = "ε"
        Zeta = "ζ"
        Eta = "η"
        Theta = "θ"
        Iota = "ι"
        Kappa = "κ"
        Lambda = "λ"
        Mu = "μ"
        Nu = "ν"
        Xi = "ξ"
        Omicron = "ο"
        Pi = "π"
        Rho = "ρ"
        Sigma = "σ"
        Tau = "τ"
        Upsilon = "υ"
        Phi = "φ"
        Chi = "χ"
        Psi = "ψ"
        Omega = "ω"
        CapitalAlpha = "Α"
        CapitalBeta = "Β"
        CapitalGamma = "Γ"
        CapitalDelta = "Δ"
        CapitalEpsilon = "Ε"
        CapitalZeta = "Ζ"
        CapitalEta = "Η"
        CapitalTheta = "Θ"
        CapitalIota = "Ι"
        CapitalKappa = "Κ"
        CapitalLambda = "Λ"
        CapitalMu = "Μ"
        CapitalNu = "Ν"
        CapitalXi = "Ξ"
        CapitalOmicron = "Ο"
        CapitalPi = "Π"
        CapitalRho = "Ρ"
        CapitalSigma = "Σ"
        CapitalTau = "Τ"
        CapitalUpsilon = "Υ"
        CapitalPhi = "Φ"
        CapitalChi = "Χ"
        CapitalPsi = "Ψ"
        CapitalOmega = "Ω"

        # Currency Symbols
        Dollar = "＄"
        Euro = "€"
        Pound = "£"
        Yen = "¥"
        Rupee = "₹"
        Won = "₩"
        Bitcoin = "₿"

        # Currency symbols
        Cent = "¢"
        Yuan = "¥"
        Ruble = "₽"
        Lira = "₺"
        Rial = "﷼"
        Baht = "฿"
        Dong = "₫"
        Naira = "₦"
        Cedi = "₵"
        Guarani = "₲"
        Colon = "₡"
        Cruzeiro = "₢"
        Franc = "₣"
        Peseta = "₧"
        Tugrik = "₮"
        Drachma = "₯"
        Penny = "₰"
        Austral = "₳"
        Hryvnia = "₴"
        Spesmilo = "₷"
        Tenge = "₸"
        Mill = "₥"
        Lari = "₾"
        Manat = "₼"

        # Technical Symbols
        Copyright = "©"
        Registered = "®"
        Trademark = "™"
        Degree = "°"
        Micro = "µ"
        Ohm = "Ω"
        Alpha = "α"
        Beta = "β"

        # Technical symbols
        ServiceMark = "℠"
        SoundRecording = "℗"
        Copyleft = "🄯"
        CareOf = "℅"
        AccountOf = "℀"
        Attention = "℁"
        Telephone = "℡"
        Facsimile = "℻"
        PerMille = "‰"
        PerTenThousand = "‱"
        Prime = "′"
        DoublePrime = "″"
        TriplePrime = "‴"
        QuadruplePrime = "⁗"
        SuperscriptOne = "¹"
        SuperscriptTwo = "²"
        SuperscriptThree = "³"
        SuperscriptPlus = "⁺"
        SuperscriptMinus = "⁻"
        SuperscriptEqual = "⁼"
        SuperscriptLeftParen = "⁽"
        SuperscriptRightParen = "⁾"
        SubscriptZero = "₀"
        SubscriptOne = "₁"
        SubscriptTwo = "₂"
        SubscriptThree = "₃"
        SubscriptPlus = "₊"
        SubscriptMinus = "₋"
        SubscriptEqual = "₌"
        SubscriptLeftParen = "₍"
        SubscriptRightParen = "₎"

        # Music symbols
        DoubleSharp = "𝄪"
        DoubleFlat = "𝄫"
        CommonTime = "𝄴"
        CutTime = "𝄵"
        Crescendo = "𝆒"
        Decrescendo = "𝆓"
        Repeat = "𝄇"
        RepeatOne = "𝄎"
        Segno = "𝄋"
        Coda = "𝄌"
        Fermata = "𝄐"
        BreathMark = "𝄒"
        Caesura = "𝄁"
        Accent = "𝆏"
        Staccato = "𝆍"
        Tenuto = "𝆏"
        Marcato = "𝆎"
        Trill = "𝆖"
        Turn = "𝆗"
        Mordent = "𝆘"
        Arpeggio = "𝆙"
        Glissando = "𝆚"
        Pedal = "𝆛"
        Piano = "𝆏"
        Forte = "𝆑"
        Mezzo = "𝆒"
        Rinforzando = "𝆔"
        Sforzando = "𝆕"

        # Weather Symbols
        Cloudy = "☁"
        Sunny = "☀"
        Rainy = "☂"
        Snowy = "☃"
        Thunder = "⚡"
        Umbrella = "☔"

        # Weather symbols
        SunBehindCloud = "⛅"
        SunBehindRainCloud = "⛆"
        CloudWithRain = "🌧"
        CloudWithSnow = "🌨"
        CloudWithLightning = "🌩"
        CloudWithTornado = "🌪"
        Fog = "🌫"
        WindFace = "🌬"
        Thermometer = "🌡"
        Droplet = "💧"
        WaterWave = "🌊"
        HighVoltage = "⚡"
        Fire = "🔥"
        Snowflake = "❄"
        Snowman = "☃"
        Comet = "☄"
        Star = "⭐"
        GlowingStar = "🌟"
        ShootingStar = "🌠"
        SunWithFace = "🌞"
        MoonWithFace = "🌝"
        NewMoon = "🌑"
        WaxingCrescentMoon = "🌒"
        FirstQuarterMoon = "🌓"
        WaxingGibbousMoon = "🌔"
        FullMoon = "🌕"
        WaningGibbousMoon = "🌖"
        LastQuarterMoon = "🌗"
        WaningCrescentMoon = "🌘"
        CrescentMoon = "🌙"

        # Office and business
        OfficeBuilding = "🏢"
        Factory = "🏭"
        DepartmentStore = "🏬"
        JapanesePostOffice = "🏣"
        EuropeanPostOffice = "🏤"
        Hospital = "🏥"
        Bank = "🏦"
        Hotel = "🏨"
        ConvenienceStore = "🏪"
        School = "🏫"
        University = "🏛"
        Church = "⛪"
        Mosque = "🕌"
        Synagogue = "🕍"
        ShintoShrine = "⛩"
        Kaaba = "🕋"
        Fountain = "⛲"
        Tent = "⛺"
        Foggy = "🌁"
        NightWithStars = "🌃"
        Cityscape = "🏙"
        SunriseOverMountains = "🌄"
        Sunrise = "🌅"
        CityscapeAtDusk = "🌆"
        Sunset = "🌇"
        BridgeAtNight = "🌉"
        HotSprings = "♨"
        Milestone = "🗿"
        Moyai = "🗿"
        StatueOfLiberty = "🗽"

        # Transportation
        Rocket = "🚀"
        Helicopter = "🚁"
        SteamLocomotive = "🚂"
        RailwayCar = "🚃"
        HighSpeedTrain = "🚄"
        BulletTrain = "🚅"
        Train = "🚆"
        Metro = "🚇"
        LightRail = "🚈"
        Station = "🚉"
        Tram = "🚊"
        Monorail = "🚝"
        MountainRailway = "🚞"
        TramCar = "🚋"
        Bus = "🚌"
        OncomingBus = "🚍"
        Trolleybus = "🚎"
        Minibus = "🚐"
        Ambulance = "🚑"
        FireEngine = "🚒"
        PoliceCar = "🚓"
        OncomingPoliceCar = "🚔"
        Taxi = "🚕"
        OncomingTaxi = "🚖"
        Automobile = "🚗"
        OncomingAutomobile = "🚘"
        SportUtilityVehicle = "🚙"
        DeliveryTruck = "🚚"
        ArticulatedLorry = "🚛"
        Tractor = "🚜"
        RacingCar = "🏎"
        Motorcycle = "🏍"
        MotorScooter = "🛵"
        Bicycle = "🚲"
        KickScooter = "🛴"
        Skateboard = "🛹"
        BusStop = "🚏"
        Motorway = "🛣"
        RailwayTrack = "🛤"
        FuelPump = "⛽"
        PoliceCarLight = "🚨"
        HorizontalTrafficLight = "🚥"
        VerticalTrafficLight = "🚦"
        StopSign = "🛑"
        Construction = "🚧"
        Anchor = "⚓"
        Sailboat = "⛵"
        Canoe = "🛶"
        Speedboat = "🚤"
        PassengerShip = "🛳"
        Ferry = "⛴"
        MotorBoat = "🛥"
        Ship = "🚢"
        Airplane = "✈"
        SmallAirplane = "🛩"
        AirplaneDeparture = "🛫"
        AirplaneArrival = "🛬"
        Seat = "💺"
        Satellite = "🛰"
        UFO = "🛸"
        FlyingSaucer = "🛸"

        # Technology and devices
        DesktopComputer = "🖥"
        LaptopComputer = "💻"
        ComputerDisk = "💽"
        FloppyDisk = "💾"
        OpticalDisk = "💿"
        DVD = "📀"
        ComputerMouse = "🖱"
        Trackball = "🖲"
        Joystick = "🕹"
        Keyboard = "⌨"
        Printer = "🖨"
        ThreeButtonMouse = "🖱"
        OneButtonMouse = "🖰"
        Scanner = "📠"
        Projector = "📽"
        Television = "📺"
        Camera = "📷"
        VideoCamera = "📹"
        MovieCamera = "🎥"
        FilmProjector = "📽"
        ClapperBoard = "🎬"
        TelevisionScreen = "📺"
        Radio = "📻"
        Videocassette = "📼"
        TelephoneReceiver = "📞"
        Pager = "📟"
        FaxMachine = "📠"
        SatelliteAntenna = "📡"
        Loudspeaker = "📢"
        Megaphone = "📣"
        Bell = "🔔"
        BellWithSlash = "🔕"
        MusicalScore = "🎼"
        MusicalNote = "🎵"
        MusicalNotes = "🎶"
        StudioMicrophone = "🎙"
        LevelSlider = "🎚"
        ControlKnobs = "🎛"
        Microphone = "🎤"
        Headphone = "🎧"
        RadioReceiver = "📻"
        MobilePhone = "📱"
        MobilePhoneWithArrow = "📲"
        Telephone = "☎"
        TelephoneLocation = "📞"
        TelephoneCompass = "📞"
        PagerLocation = "📟"
        FaxLocation = "📠"
        SatelliteLocation = "📡"

        # Security and permissions
        LockWithInkPen = "🔏"
        ClosedLockWithKey = "🔐"
        Key = "🔑"
        OldKey = "🗝"
        Hammer = "🔨"
        Pick = "⛏"
        HammerAndPick = "⚒"
        HammerAndWrench = "🛠"
        Dagger = "🗡"
        CrossedSwords = "⚔"
        Pistol = "🔫"
        BowAndArrow = "🏹"
        Shield = "🛡"
        Wrench = "🔧"
        NutAndBolt = "🔩"
        Gear = "⚙"
        Compression = "🗜"
        Scales = "⚖"
        Link = "🔗"
        BrokenChain = "🔗"
        Chains = "⛓"
        Hook = "🪝"
        Toolbox = "🧰"
        Magnet = "🧲"
        TestTube = "🧪"
        PetriDish = "🧫"
        DNA = "🧬"
        Microscope = "🔬"
        Telescope = "🔭"
        SatelliteAntenna = "📡"
        Syringe = "💉"
        Pill = "💊"
        Door = "🚪"
        Bed = "🛏"
        CouchAndLamp = "🛋"
        Toilet = "🚽"
        Shower = "🚿"
        Bathtub = "🛁"
        Razor = "🪒"
        LotionBottle = "🧴"
        SafetyPin = "🧷"
        Broom = "🧹"
        Basket = "🧺"
        RollOfPaper = "🧻"
        Soap = "🧼"
        Sponge = "🧽"
        FireExtinguisher = "🧯"
        ShoppingCart = "🛒"
        Cigarette = "🚬"
        Coffin = "⚰"
        FuneralUrn = "⚱"
        Moai = "🗿"
        Placard = "🪧"
        IdentificationCard = "🪪"

        # Food and beverages
        Grapes = "🍇"
        Melon = "🍈"
        Watermelon = "🍉"
        Tangerine = "🍊"
        Lemon = "🍋"
        Banana = "🍌"
        Pineapple = "🍍"
        Mango = "🥭"
        RedApple = "🍎"
        GreenApple = "🍏"
        Pear = "🍐"
        Peach = "🍑"
        Cherries = "🍒"
        Strawberry = "🍓"
        KiwiFruit = "🥝"
        Tomato = "🍅"
        Coconut = "🥥"
        Avocado = "🥑"
        Eggplant = "🍆"
        Potato = "🥔"
        Carrot = "🥕"
        EarOfCorn = "🌽"
        HotPepper = "🌶"
        Cucumber = "🥒"
        LeafyGreen = "🥬"
        Broccoli = "🥦"
        Garlic = "🧄"
        Onion = "🧅"
        Mushroom = "🍄"
        Peanuts = "🥜"
        Chestnut = "🌰"
        Bread = "🍞"
        Croissant = "🥐"
        BaguetteBread = "🥖"
        Pretzel = "🥨"
        Bagel = "🥯"
        Pancakes = "🥞"
        Waffle = "🧇"
        CheeseWedge = "🧀"
        MeatOnBone = "🍖"
        PoultryLeg = "🍗"
        CutOfMeat = "🥩"
        Bacon = "🥓"
        Hamburger = "🍔"
        FrenchFries = "🍟"
        Pizza = "🍕"
        HotDog = "🌭"
        Sandwich = "🥪"
        Taco = "🌮"
        Burrito = "🌯"
        StuffedFlatbread = "🥙"
        Falafel = "🧆"
        Egg = "🥚"
        Cooking = "🍳"
        ShallowPanOfFood = "🥘"
        PotOfFood = "🍲"
        BowlWithSpoon = "🥣"
        GreenSalad = "🥗"
        Popcorn = "🍿"
        Butter = "🧈"
        Salt = "🧂"
        CannedFood = "🥫"
        BentoBox = "🍱"
        RiceCracker = "🍘"
        RiceBall = "🍙"
        CookedRice = "🍚"
        CurryRice = "🍛"
        SteamingBowl = "🍜"
        Spaghetti = "🍝"
        RoastedSweetPotato = "🍠"
        Oden = "🍢"
        Sushi = "🍣"
        FriedShrimp = "🍤"
        FishCakeWithSwirl = "🍥"
        MoonCake = "🥮"
        Dango = "🍡"
        Dumpling = "🥟"
        FortuneCookie = "🥠"
        TakeoutBox = "🥡"
        Crab = "🦀"
        Lobster = "🦞"
        Shrimp = "🦐"
        Squid = "🦑"
        Oyster = "🦪"
        IceCream = "🍨"
        ShavedIce = "🍧"
        SoftIceCream = "🍦"
        Doughnut = "🍩"
        Cookie = "🍪"
        BirthdayCake = "🎂"
        Shortcake = "🍰"
        Cupcake = "🧁"
        Pie = "🥧"
        ChocolateBar = "🍫"
        Candy = "🍬"
        Lollipop = "🍭"
        Custard = "🍮"
        HoneyPot = "🍯"
        BabyBottle = "🍼"
        GlassOfMilk = "🥛"
        HotBeverage = "☕"
        TeacupWithoutHandle = "🍵"
        Sake = "🍶"
        BottleWithPoppingCork = "🍾"
        WineGlass = "🍷"
        CocktailGlass = "🍸"
        TropicalDrink = "🍹"
        BeerMug = "🍺"
        ClinkingBeerMugs = "🍻"
        ClinkingGlasses = "🥂"
        TumblerGlass = "🥃"
        CupWithStraw = "🥤"
        BeverageBox = "🧃"
        Mate = "🧉"
        Ice = "🧊"
        Chopsticks = "🥢"
        ForkAndKnifeWithPlate = "🍽"
        ForkAndKnife = "🍴"
        Spoon = "🥄"
        KitchenKnife = "🔪"
        Amphora = "🏺"

        # Sports and entertainment
        SoccerBall = "⚽"
        Basketball = "🏀"
        AmericanFootball = "🏈"
        Baseball = "⚾"
        Softball = "🥎"
        Tennis = "🎾"
        Volleyball = "🏐"
        RugbyFootball = "🏉"
        FlyingDisc = "🥏"
        Bowling = "🎳"
        CricketGame = "🏏"
        FieldHockey = "🏑"
        IceHockey = "🏒"
        Lacrosse = "🥍"
        PingPong = "🏓"
        Badminton = "🏸"
        BoxingGlove = "🥊"
        MartialArtsUniform = "🥋"
        GoalNet = "🥅"
        FlagInHole = "⛳"
        IceSkate = "⛸"
        FishingPole = "🎣"
        RunningShirt = "🎽"
        Skis = "🎿"
        Sled = "🛷"
        CurlingStone = "🥌"
        DirectHit = "🎯"
        YoYo = "🪀"
        Kite = "🪁"
        Pool8Ball = "🎱"
        CrystalBall = "🔮"
        MagicWand = "🪄"
        VideoGame = "🎮"
        Joystick = "🕹"
        SlotMachine = "🎰"
        GameDie = "🎲"
        PuzzlePiece = "🧩"
        TeddyBear = "🧸"
        Piñata = "🪅"
        NestingDolls = "🪆"
        SpadeSuit = "♠"
        HeartSuit = "♥"
        DiamondSuit = "♦"
        ClubSuit = "♣"
        ChessPawn = "♟"
        Joker = "🃏"
        MahjongRedDragon = "🀄"
        FlowerPlayingCards = "🎴"
        PerformingArts = "🎭"
        FramedPicture = "🖼"
        ArtistPalette = "🎨"
        Thread = "🧵"
        Yarn = "🧶"
        Glasses = "👓"
        Sunglasses = "🕶"
        Goggles = "🥽"
        LabCoat = "🥼"
        SafetyVest = "🦺"
        Necktie = "👔"
        TShirt = "👕"
        Jeans = "👖"
        Scarf = "🧣"
        Gloves = "🧤"
        Coat = "🧥"
        Socks = "🧦"
        Dress = "👗"
        Kimono = "👘"
        Sari = "🥻"
        OnePieceSwimsuit = "🩱"
        Briefs = "🩲"
        Shorts = "🩳"
        Bikini = "👙"
        WomansClothes = "👚"
        Purse = "👛"
        Handbag = "👜"
        ClutchBag = "👝"
        ShoppingBags = "🛍"
        Backpack = "🎒"
        MansShoe = "👞"
        RunningShoe = "👟"
        HikingBoot = "🥾"
        FlatShoe = "🥿"
        HighHeeledShoe = "👠"
        WomansSandal = "👡"
        BalletShoes = "🩰"
        WomansBoot = "👢"
        Crown = "👑"
        WomansHat = "👒"
        TopHat = "🎩"
        GraduationCap = "🎓"
        BilledCap = "🧢"
        RescueWorkersHelmet = "⛑"
        PrayerBeads = "📿"
        Lipstick = "💄"
        Ring = "💍"
        GemStone = "💎"

        # arrow symbols
        BoxArrowRight = "⊸"   #  (U+22B8)
        BoxArrowLeft = "⊷"    #  (U+22B7)
        BoxArrowUp = "⟰"      #  (U+27F0)
        BoxArrowDown = "⟱"    #  (U+27F1)

        # math symbols
        UnionBox = "⊌"     #  (U+228C)
        IntersectionBox = "⊍"  #  (U+228D)

        # logic symbols
        AndBox = "∧"       # 
        OrBox = "∨"        # 

        SetUnion = "∪"            # 
        SetIntersection = "∩"     # 
        SetDifference = "∖"       # 
        SetSymmetricDifference = "△"  # (U+2206)

        BoxExclamation = "⍢"      #  (U+2362)
        BoxInfo = "⍟"             #  (U+235F)
        BoxWarning = "⚠"          #  (U+26A0)

        
"""
